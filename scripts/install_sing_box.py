#!/usr/bin/env python3
"""Install the pinned official Linux CLI for compile/decompile only, verifying SHA-256."""
import argparse
import hashlib
from pathlib import Path
import shutil
import tarfile
import urllib.request

VERSION="1.14.4"
SHA256="699a1b510aa4396b2176d32d1181920399ebf1e267835da6f3b598d0f7c24968"
URL=f"https://github.com/SagerNet/sing-box/releases/download/v{VERSION}/sing-box-{VERSION}-linux-amd64.tar.gz"

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--directory",required=True);args=p.parse_args()
    directory=Path(args.directory).resolve();directory.mkdir(parents=True,exist_ok=True)
    archive=directory/"sing-box.tar.gz"
    with urllib.request.urlopen(URL,timeout=120) as src, archive.open("wb") as dst:shutil.copyfileobj(src,dst)
    with archive.open("rb") as f:actual=hashlib.file_digest(f,"sha256").hexdigest()
    if actual!=SHA256:raise SystemExit("Official sing-box archive checksum mismatch")
    with tarfile.open(archive,"r:gz") as tar:
        members=[m for m in tar.getmembers() if m.isfile() and m.name.endswith("/sing-box")]
        if len(members)!=1:raise SystemExit("Unexpected sing-box archive layout")
        with tar.extractfile(members[0]) as src,(directory/"sing-box").open("wb") as dst:shutil.copyfileobj(src,dst)
    (directory/"sing-box").chmod(0o755)
    print(directory/"sing-box")
