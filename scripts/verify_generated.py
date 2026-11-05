#!/usr/bin/env python3
"""Validate the complete publication before it can replace the last good release."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import urllib.parse
from build_catalog import validate_manifest

def verify(directory: Path, repository: str):
    manifest=json.loads((directory/'lists.json').read_text(encoding='utf-8'))
    metadata=json.loads((directory/'services.json').read_text(encoding='utf-8'))
    details=metadata['services']
    validate_manifest(manifest,details)
    prefix=f'https://raw.githubusercontent.com/{repository}/release/'
    by_key={item['key']:item for item in details}
    for entry in manifest['domain_lists']+manifest['categories']:
        if not entry['url'].startswith(prefix):raise ValueError('Rule URL leaves the publication repository')
        relative=PurePosixPath(urllib.parse.unquote(entry['url'][len(prefix):]))
        if relative.is_absolute() or '..' in relative.parts:raise ValueError('Unsafe rule path')
        target=directory.joinpath(*relative.parts)
        with target.open('rb') as f:
            if f.read(3)!=b'SRS':raise ValueError('Invalid SRS: '+str(relative))
        detail=by_key[entry['id']]
        for field in ('documentation','details_json','details_text'):
            if not (directory/detail[field]).is_file():raise ValueError('Missing detail: '+entry['id'])
        if entry['count']!=detail['counts']['total']:raise ValueError('Rule count mismatch')
    discord=json.loads((directory/'details/da_discord_quests.json').read_text(encoding='utf-8'))
    if 'hcaptcha.com' not in discord['rules'][0]['domain_suffix']:raise ValueError('Discord captcha route missing')
    nvidia=json.loads((directory/'details/da_nvidia_app.json').read_text(encoding='utf-8'))
    for rule in nvidia['rules']:
        for field in ('domain','domain_suffix'):
            if any(s==bad or s.endswith('.'+bad) for s in rule.get(field,[]) for bad in ('huggingface.co','hf.co','hf.space')):
                raise ValueError('Unrelated Hugging Face domain in NVIDIA App profile')
    checked=0
    for line in (directory/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest,name=line.split('  ',1)
        relative=PurePosixPath(name)
        if relative.is_absolute() or '..' in relative.parts:raise ValueError('Unsafe checksum path')
        with directory.joinpath(*relative.parts).open('rb') as f:actual=hashlib.file_digest(f,'sha256').hexdigest()
        if actual!=digest:raise ValueError('Publication checksum mismatch: '+name)
        checked+=1
    expected={p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'}
    listed={line.split('  ',1)[1] for line in (directory/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()}
    if listed!=expected:raise ValueError('Checksum coverage is incomplete')
    print(f'Verified {len(details)} catalog entries and {checked} file checksums')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--repository',required=True)
    args=p.parse_args();verify(args.directory,args.repository)
