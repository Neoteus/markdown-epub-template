@echo off
setlocal EnableDelayedExpansion
SET md=
FOR /R %%I IN (*.md) DO IF NOT %%~nI==README set md=!md! %%I
echo Working...
pandoc --toc --resource-path ./images -o book.epub%md%
echo Complete!
pause
