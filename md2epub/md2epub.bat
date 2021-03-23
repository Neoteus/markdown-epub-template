@echo off
setlocal EnableDelayedExpansion
SET md=
FOR /R %%I IN (markdown\*.md) DO set md=!md! %%I
echo Working...
pandoc --toc --epub-embed-font=font\open-sans-v17-latin-ext_latin-*.woff2 -o book.epub title.md%md%
echo Complete!
pause
