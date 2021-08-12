#!/usr/bin/python3
import os
import subprocess

OUTPUT = 'book.epub'
TITLE = 'title.md'
CONTENT = 'markdown'

def ls_md(path):
    md = []
    with os.scandir(path) as entrys:
        for e in entrys:
            if e.is_file() and e.name.endswith('.md'):
                md.append(e.path)
            elif e.is_dir():
                md += ls_md(e.path)
    return md
contents = ls_md(CONTENT)

args = ['pandoc', '--toc']
args.append('-o')
args.append(OUTPUT)
args.append(TITLE)
args += contents

print('Input MarkDown (the order is listed below):\n  {}'.format(TITLE))
for i in contents:
    print('  ' + i)
subprocess.Popen(args)
print('\nOutput EPUB:\n  {}'.format(OUTPUT))
