@echo off
setlocal EnableDelayedExpansion
SET md=
FOR /R %%I IN (markdown\*.md) DO set md=!md! %%I
echo Input MarkDown (the order is listed below):
FOR /R %%I IN (markdown\*.md) DO echo %%I
pandoc --toc -o book.epub title.md%md%
echo.
echo Output EPUB:
echo book.epub
pause
