@echo off
ebook-convert book.md book.epub --output-profile tablet --formatting-type markdown --markdown-extensions codehilite,footnotes,meta,tables,toc --paragraph-type off --cover .\images\cover.png
pause
