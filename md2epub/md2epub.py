#!/usr/bin/python3
import os

OUTPUT_FILE = './book.epub'
TITLE_FILE = './title.md'
EMBED_FONT = ['./font/open-sans-v17-latin-ext_latin-*.woff2']

def ls_md(path='./markdown'):
    md = []
    with os.scandir(path) as entrys:
        for e in entrys:
            if e.is_file() and e.name.endswith('.md'):
                md.append(e.path)
            elif e.is_dir():
                md += ls_md(e.path)
    return md

args = ['--toc']
for i in EMBED_FONT:
    args.append(f'--epub-embed-font={i}')
if OUTPUT_FILE:
    args.append('-o')
    args.append(OUTPUT_FILE)
if TITLE_FILE:
    args.append(TITLE_FILE)
content_md = ls_md()
args += content_md

print('Input MarkDonw:\n  title.md')
for i in content_md:
    print('  ' + i)
os.system('pandoc ' + ' '.join(args))
print(f'Output EPUB:\n  {OUTPUT_FILE}')
