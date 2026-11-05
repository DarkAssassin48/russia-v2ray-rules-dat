#!/usr/bin/env python3
"""Mirror an immutable runetfreedom release and build an auditable Forkozz catalog."""
from __future__ import annotations

import argparse
import concurrent.futures
import contextlib
import datetime as dt
import hashlib
import itertools
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import threading
import time
import urllib.parse
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "runetfreedom/russia-v2ray-rules-dat"
KINDS = {"domain":"exact", "domain_suffix":"suffix", "domain_keyword":"keyword", "domain_regex":"regex", "ip_cidr":"ip"}
SAFE_REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

def request(url: str):
    headers = {"User-Agent":"DarkAssassin-Forkozz-Catalog/1.0"}
    if urllib.parse.urlsplit(url).hostname == "api.github.com":
        headers["Accept"] = "application/vnd.github+json"
        if os.environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    return opener.open(urllib.request.Request(url, headers=headers), timeout=120)

def download(url: str, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    last = None
    for attempt in range(4):
        try:
            with request(url) as response, dest.with_suffix(dest.suffix + ".part").open("wb") as target:
                shutil.copyfileobj(response, target)
            dest.with_suffix(dest.suffix + ".part").replace(dest)
            return
        except Exception as error:
            last = error
            if attempt < 3: time.sleep(2 ** attempt)
    raise RuntimeError(f"Download failed: {url}") from last

def snapshot(cache: Path, workspace: Path):
    with request(f"https://api.github.com/repos/{UPSTREAM}/commits/release") as response:
        commit = json.load(response)
    sha = commit["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", sha): raise ValueError("Invalid upstream commit")
    archive = cache / (sha + ".zip")
    if not archive.is_file(): download(f"https://codeload.github.com/{UPSTREAM}/zip/{sha}", archive)
    target = workspace / "upstream"
    target.mkdir(parents=True, exist_ok=False)
    total = 0
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            parts = PurePosixPath(info.filename).parts[1:]
            if not parts or info.is_dir(): continue
            if any(part in (".", "..") for part in parts) or PurePosixPath(*parts).is_absolute():
                raise ValueError("Unsafe archive path")
            if stat.S_ISLNK(info.external_attr >> 16): raise ValueError("Archive symlink rejected")
            path = PurePosixPath(*parts).as_posix()
            wanted = path in ("geoip.dat", "geoip.dat.sha256sum", "geosite.dat", "geosite.dat.sha256sum") or (
                len(parts) == 3 and parts[0] == "sing-box" and parts[1] in ("rule-set-geosite", "rule-set-geoip") and parts[2].endswith(".srs"))
            if not wanted: continue
            total += info.file_size
            if total > 512 * 1024 * 1024 or info.file_size > 100 * 1024 * 1024:
                raise ValueError("Upstream snapshot exceeds publication limits")
            dest = target.joinpath(*parts)
            dest.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, dest.open("wb") as dst: shutil.copyfileobj(src, dst)
    for name in ("geoip.dat", "geosite.dat"):
        checksum = (target / (name + ".sha256sum")).read_text().split()[0]
        actual = hashlib.file_digest((target / name).open("rb"), "sha256").hexdigest()
        if actual != checksum: raise ValueError(f"Upstream checksum mismatch: {name}")
    files = sorted(target.glob("sing-box/*/*.srs"))
    if len(files) < 1000: raise ValueError("Incomplete upstream rule-set snapshot")
    return target, {"repository":UPSTREAM,"commit":sha,"commit_date":commit["commit"]["committer"]["date"],"archive_sha256":hashlib.file_digest(archive.open("rb"),"sha256").hexdigest()}

def identifier(kind: str, stem: str):
    clean = re.sub(r"[^a-z0-9_]", "_", stem.lower())[:64]
    return "rf_" + kind + "_" + clean + "_" + hashlib.sha256(stem.encode()).hexdigest()[:8]

def conditions(rules, prefix=""):
    for i, rule in enumerate(rules):
        here = f"{prefix}rules[{i}]"
        if rule.get("type") == "logical":
            yield from conditions(rule.get("rules", []), here + ".")
        for key, value in rule.items():
            if key in ("type", "mode", "rules", "invert"): continue
            for entry in value if isinstance(value, list) else [value]:
                yield here, key, entry

def summarize(doc):
    counts = {value:0 for value in KINDS.values()}
    unknown = set()
    for _, field, _ in conditions(doc["rules"]):
        if field in KINDS: counts[KINDS[field]] += 1
        else: unknown.add(field)
    counts["total"] = sum(counts.values())
    return counts, sorted(unknown)

def markdown_safe(value): return str(value).replace("|", "\\|").replace("\n", " ")

def full_text(doc):
    yield "# Точный состав правил. domain_suffix включает домен и все его поддомены.\n"
    yield "# domain — только точное имя; domain_keyword — фрагмент; domain_regex — регулярное выражение; ip_cidr — сеть.\n"
    yield "# Для логических комбинаций и исключений используйте полный JSON: он сохраняет исходную структуру.\n"
    for group, key, value in conditions(doc["rules"]):
        yield f"{group}\t{key}\t{json.dumps(value, ensure_ascii=False) if not isinstance(value,str) else value}\n"

def detail_files(output: Path, item, doc):
    stem = item["key"]
    json_path = output / "details" / (stem + ".json")
    text_path = output / "details" / (stem + ".txt")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(json_path, doc)
    with text_path.open("w", encoding="utf-8", newline="\n") as f: f.writelines(full_text(doc))
    counts, unknown = summarize(doc)
    item.update(counts=counts, unknown_matchers=unknown, details_json="details/"+stem+".json", details_text="details/"+stem+".txt", documentation="docs/"+stem+".md")
    lines = [f"# {item['name_ru']}", "", item["description_ru"], "", f"Код: `{item['original_code']}`. Тип: **{item['kind']}**.", "",
        f"Правил: **{counts['total']}**. Точные домены: {counts['exact']}; доменные зоны: {counts['suffix']}; фрагменты: {counts['keyword']}; regex: {counts['regex']}; IP-сети: {counts['ip']}.", "",
        "## Полный состав", "", f"- [Все адреса в текстовом виде](../{item['details_text']})", f"- [Полный JSON с исходной логикой](../{item['details_json']})", f"- [Готовый SRS](../{item['rule_path']})", "",
        "`domain_suffix` охватывает сам домен и все поддомены. Точное правило `domain` охватывает только указанное имя. IP-набор может направлять через VPN несколько сервисов, использующих одну сеть.", "",
        "## Первые адреса", "", "```text"]
    for _, key, value in itertools.islice(conditions(doc["rules"]),50): lines.append(f"{key}: {value}")
    lines.extend(["```", "", "Полный перечень без сокращений доступен по ссылкам выше.", "", "По умолчанию выключен. Добавление каталога само по себе не включает маршрут.", ""])
    if unknown: lines.extend(["Дополнительные поля сохранены в JSON: "+", ".join(unknown), ""])
    path = output / item["documentation"];path.parent.mkdir(parents=True,exist_ok=True);path.write_text("\n".join(lines),encoding="utf-8")

def compose_profile(profile, docs):
    fields = {}
    for base in profile.get("bases", []):
        doc = docs[base]
        if any(rule.get("type") == "logical" or rule.get("invert") for rule in doc["rules"]):
            raise ValueError("Curated profile cannot flatten logical/inverted source: "+base)
        for rule in doc["rules"]:
            for key, values in rule.items():
                if key not in KINDS or key == "ip_cidr": raise ValueError("Unexpected profile matcher: "+key)
                fields.setdefault(key,set()).update(values)
    for key, config in (("domain_suffix","add_suffix"),("domain","add_domain")):
        fields.setdefault(key,set()).update(profile.get(config,[]))
    excluded = profile.get("exclude_suffix",[])
    if excluded:
        for key in ("domain", "domain_suffix"):
            fields[key]={s for s in fields.get(key,set()) if not any(s==bad or s.endswith("."+bad) for bad in excluded)}
    return {"version":1,"rules":[{key:sorted(values) for key,values in sorted(fields.items()) if values}]}

def validate_manifest(doc, details):
    entries=doc["domain_lists"]+doc["categories"]
    ids=[entry["id"] for entry in entries]
    native=[re.sub(r"[^a-z0-9_]","_",re.sub(r"^svc_","",key.lower())) for key in ids]
    if len(set(ids))!=len(ids) or len(set(native))!=len(native):raise ValueError("Catalog identifiers collide")
    for entry in entries:
        if entry.get("default_on") is not False:raise ValueError("Catalog may not auto-enable traffic")
        url=urllib.parse.urlsplit(entry["url"])
        trusted_host=url.hostname=="raw.githubusercontent.com" or bool(re.fullmatch(r"[a-z0-9-]+\.github\.io",url.hostname or ""))
        if entry["format"]!="srs" or url.scheme!="https" or not trusted_host or url.username or url.password:raise ValueError("Unexpected rule URL")
        if not entry.get("source_name"):raise ValueError("Forkozz requires a provider group")
    if len(entries)!=len(details):raise ValueError("Catalog and details differ")

def compact_manifest(manifest, repository, profiles_only=False):
    """Keep native parser fields and stable IDs; move binary downloads to Pages."""
    old_base=f"https://raw.githubusercontent.com/{repository}/release"
    owner,name=repository.split("/")
    new_base=f"https://{owner.lower()}.github.io/{name}"
    result={key:manifest[key] for key in ("version","generated_at")}
    result.update(base_url=new_base,categories=[],domain_lists=[])
    for kind in ("categories","domain_lists"):
        for entry in manifest[kind]:
            if profiles_only and not entry["id"].startswith("da_"):continue
            if not entry["url"].startswith(old_base+"/"):raise ValueError("Unexpected original rule URL")
            slim={key:entry[key] for key in ("id","name_ru","format","source_name","default_on")}
            slim["url"]=new_base+entry["url"][len(old_base):]
            result[kind].append(slim)
    validate_manifest(result,result["categories"]+result["domain_lists"])
    return result

def build_pages_distribution(source, target, repository):
    """Publish only catalogs and SRS (~31 MB); keep large reference exports in Git."""
    target.mkdir(parents=True,exist_ok=True)
    if any(target.iterdir()):raise ValueError("Pages output must be empty")
    manifest=json.loads((source/"lists.json").read_text(encoding="utf-8"))
    for filename,profiles_only in (("lists.json",False),("lists-lite.json",True)):
        write_json(target/filename,compact_manifest(manifest,repository,profiles_only))
    for folder in ("sing-box","custom"):
        shutil.copytree(source/folder,target/folder)
    (target/".nojekyll").write_text("",encoding="utf-8")
    info={"version":manifest["version"],"generated_at":manifest["generated_at"],"full_entries":len(manifest["categories"])+len(manifest["domain_lists"]),"lite_entries":sum(e["id"].startswith("da_") for e in manifest["domain_lists"]),"full_bytes":(target/"lists.json").stat().st_size,"lite_bytes":(target/"lists-lite.json").stat().st_size}
    write_json(target/"build-info.json",info)
    return info

def build(args):
    if not SAFE_REPO.fullmatch(args.repository):raise ValueError("Invalid publication repository")
    output=Path(args.output).resolve();workspace=Path(args.work).resolve();cache=Path(args.cache).resolve()
    for path in (output,workspace,cache):path.mkdir(parents=True,exist_ok=True)
    if any(output.iterdir()):raise ValueError("Output directory must be empty")
    upstream, provenance=snapshot(cache,workspace)
    shutil.copytree(upstream,output,dirs_exist_ok=True)
    labels=json.loads((ROOT/"catalog/labels.json").read_text(encoding="utf-8"))
    profiles=json.loads((ROOT/"catalog/profiles.json").read_text(encoding="utf-8"))
    wanted={base for p in profiles for base in p.get("bases",[])}
    base_docs={};all_details=[];large=threading.Semaphore(1)
    base_url=f"https://raw.githubusercontent.com/{args.repository}/release"
    def one(path):
        relative=path.relative_to(upstream).as_posix();stem=path.stem
        kind="domains" if path.parent.name=="rule-set-geosite" else "ip"
        original=stem.removeprefix("geosite-").removeprefix("geoip-")
        name=labels.get(original,original)+(" · IP-сети" if kind=="ip" else "")
        group="runetfreedom · IP-сети" if kind=="ip" else "runetfreedom · Категории" if original.startswith(("category-","geolocation-","ru-","antifilter","refilter")) else "runetfreedom · Сервисы"
        if path.stat().st_size>1024*1024:name+=" [большой набор]"
        key=identifier(kind,stem)
        item={"key":key,"name_ru":name,"original_code":original,"kind":kind,"source_name":group,"rule_path":relative,"srs_bytes":path.stat().st_size,"description_ru":f"Актуальный набор {'доменных правил' if kind=='domains' else 'IP-сетей'} «{labels.get(original,original)}» из runetfreedom. Полный текущий состав приведён в файлах JSON и TXT."}
        temp=workspace/"decoded"/(stem+".json");temp.parent.mkdir(parents=True,exist_ok=True)
        with large if path.stat().st_size>1024*1024 else contextlib.nullcontext():
            subprocess.run([args.sing_box,"rule-set","decompile","--output",str(temp),str(path)],check=True,capture_output=True,timeout=180)
            doc=json.loads(temp.read_text(encoding="utf-8-sig"))
            if not isinstance(doc.get("rules"),list):raise ValueError("Invalid decoded source: "+relative)
            detail_files(output,item,doc)
            if kind=="domains" and original in wanted:base_docs[original]=doc
        return item
    files=sorted(upstream.glob("sing-box/*/*.srs"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for number,item in enumerate(pool.map(one,files),1):
            all_details.append(item)
            if number%250==0:print(f"Documented {number}/{len(files)} upstream rule sets",flush=True)
    curated=[]
    for profile in profiles:
        doc=compose_profile(profile,base_docs)
        relative="custom/"+profile["id"]+".srs";src=workspace/"profiles"/(profile["id"]+".json");write_json(src,doc)
        target=output/relative;target.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run([args.sing_box,"rule-set","compile","--output",str(target),str(src)],check=True,capture_output=True,timeout=45)
        item={"key":"da_"+profile["id"].replace("-","_"),"name_ru":profile["name_ru"],"original_code":profile["id"],"kind":"domains","source_name":"DarkAssassin · Готовые профили","rule_path":relative,"srs_bytes":target.stat().st_size,"description_ru":profile["description_ru"],"bases":profile.get("bases",[]),"exclude_suffix":profile.get("exclude_suffix",[])}
        detail_files(output,item,doc);curated.append(item)
    all_details=curated+sorted(all_details,key=lambda x:(x["source_name"],x["name_ru"].casefold()))
    generated=dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
    version=generated.replace("-","").replace(":","")+"-"+provenance["commit"][:8]
    manifest={"version":version,"generated_at":generated,"base_url":base_url,"categories":[],"domain_lists":[]}
    for item in all_details:
        entry={"id":item["key"],"name_ru":item["name_ru"],"format":"srs","url":base_url+"/"+urllib.parse.quote(item["rule_path"],safe="/@!._-"),"source":"runetfreedom","source_name":item["source_name"],"default_on":False,"count":item["counts"]["total"]}
        manifest["categories" if item["kind"]=="ip" else "domain_lists"].append(entry)
    validate_manifest(manifest,all_details)
    write_json(output/"lists.json",manifest)
    write_json(output/"services.json",{"version":version,"generated_at":generated,"upstream":provenance,"services":all_details})
    write_json(output/"build-info.json",{"version":version,"generated_at":generated,"upstream":provenance,"upstream_rule_sets":len(files),"curated_profiles":len(curated),"domain_lists":len(manifest["domain_lists"]),"ip_lists":len(manifest["categories"]),"catalog_bytes":(output/"lists.json").stat().st_size,"automatic_schedule":"every 6 hours"})
    rows=["# Каталог сервисов и адресов","",f"Собран: {generated}. Источник runetfreedom: `{provenance['commit']}`.","",f"Всего наборов: **{len(all_details)}**, из них готовых профилей: **{len(curated)}**. Все выключены по умолчанию.","","Для каждого пункта приведены описание, счётчики и ссылки на полный состав без сокращений. Исходный JSON сохраняет логические комбинации, regex и исключения.","","## Готовые профили DarkAssassin","","| Сервис | Правил | Полный состав |","|---|---:|---|"]
    for item in curated:rows.append(f"| [{markdown_safe(item['name_ru'])}]({item['documentation']}) | {item['counts']['total']} | [TXT]({item['details_text']}) · [JSON]({item['details_json']}) |")
    rows.extend(["", "## Все исходные наборы runetfreedom", "", "Каталог разбит на страницы по 200 пунктов. Для поиска по всем именам скачайте [services.json](services.json).", ""])
    groups=sorted({item['source_name'] for item in all_details if not item['key'].startswith('da_')})
    for group_no,group in enumerate(groups,1):
        entries=[item for item in all_details if item['source_name']==group]
        rows.extend([f"### {group} — {len(entries)}", ""])
        for offset in range(0,len(entries),200):
            page_no=offset//200+1
            page=f"docs/index-{group_no}-{page_no}.md"
            rows.append(f"- [Пункты {offset+1}–{min(offset+200,len(entries))}]({page})")
            page_rows=[f"# {group}","","[Вернуться к каталогу](../CATALOG.md)","","| Сервис / категория | Тип | Правил | Полный состав |","|---|---|---:|---|"]
            for item in entries[offset:offset+200]:page_rows.append(f"| [{markdown_safe(item['name_ru'])}]({Path(item['documentation']).name}) | {item['kind']} | {item['counts']['total']} | [TXT](../{item['details_text']}) · [JSON](../{item['details_json']}) |")
            (output/page).write_text("\n".join(page_rows)+"\n",encoding="utf-8")
        rows.append("")
    (output/"CATALOG.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
    shutil.copyfile(ROOT/"LICENSE",output/"LICENSE")
    shutil.copyfile(ROOT/"README.md",output/"README.md")
    shutil.copyfile(ROOT/"UPSTREAM.md",output/"UPSTREAM.md")
    with zipfile.ZipFile(output/"sing-box.zip","w",zipfile.ZIP_DEFLATED) as z:
        for path in sorted((output/"sing-box").glob("*/*.srs")):z.write(path,path.relative_to(output/"sing-box").as_posix())
    sums=[]
    for path in sorted(output.rglob("*")):
        if path.is_file():
            if path.stat().st_size>100*1024*1024:raise ValueError("Published file exceeds GitHub limit: "+str(path))
            with path.open("rb") as f:digest=hashlib.file_digest(f,"sha256").hexdigest()
            sums.append(digest+"  "+path.relative_to(output).as_posix())
    (output/"SHA256SUMS.txt").write_text("\n".join(sums)+"\n",encoding="utf-8")
    pages_info=build_pages_distribution(output,workspace/"pages",args.repository)
    print(json.dumps({"pages":pages_info},ensure_ascii=False),flush=True)
    print(json.dumps({"version":version,"services":len(all_details),"curated":len(curated),"manifest_bytes":(output/"lists.json").stat().st_size,"published_bytes":sum(p.stat().st_size for p in output.rglob("*") if p.is_file())},ensure_ascii=False),flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--repository",default="DarkAssassin48/russia-v2ray-rules-dat")
    parser.add_argument("--output",required=True)
    parser.add_argument("--work",required=True)
    parser.add_argument("--cache",required=True)
    parser.add_argument("--sing-box",required=True)
    parser.add_argument("--jobs",type=int,default=4)
    build(parser.parse_args())
