#!/usr/bin/env python3
"""Publish one verified snapshot only to the owner's fork, using a lease."""
import argparse
import json
import os
from pathlib import Path
import subprocess

OWNER_REPOSITORY='DarkAssassin48/russia-v2ray-rules-dat'

def git(directory,*args,capture=False):
    return subprocess.run(['git','-c','credential.helper=','-c','credential.helper=!gh auth git-credential',*args],cwd=directory,check=True,text=True,capture_output=capture)

def publish(directory,repository):
    if repository!=OWNER_REPOSITORY or os.environ.get('GITHUB_REPOSITORY',repository)!=repository:
        raise ValueError('Publication is restricted to the DarkAssassin48 fork')
    if (directory/'.git').exists():raise ValueError('Publication directory already contains a git repository')
    manifest=json.loads((directory/'lists.json').read_text(encoding='utf-8'))
    git(directory,'init','--initial-branch=release','--quiet')
    git(directory,'config','user.name','github-actions[bot]')
    git(directory,'config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
    git(directory,'config','core.autocrlf','false')
    git(directory,'remote','add','origin',f'https://github.com/{repository}.git')
    remote=git(directory,'ls-remote','origin','refs/heads/release',capture=True).stdout.strip()
    expected=remote.split()[0] if remote else ''
    git(directory,'add','--all')
    git(directory,'commit','--quiet','-m','Forkozz catalog '+manifest['version'])
    git(directory,'push',f'--force-with-lease=refs/heads/release:{expected}','origin','HEAD:refs/heads/release')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--repository',required=True)
    args=p.parse_args();publish(args.directory.resolve(),args.repository)
