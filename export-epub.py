#!/usr/bin/python3

import os

def get_md(path='.', exclude=()):
    md = []
    with os.scandir(path) as entrys:
        for e in entrys:
            if e.is_file() and e.name.endswith('.md') and e.name not in exclude:
                md.append(e.path)
            elif e.is_dir():
                md = md + get_md(e.path)
    return md

exclude = ('README.md', )
os.system('pandoc --toc --resource-path ./images -o book.epub {}'.format(' '.join(get_md(exclude=exclude))))
