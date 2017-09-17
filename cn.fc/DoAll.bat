@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

for /f "delims=" %%b in ('dir /b "%curp%\*.bat" ^| findstr /b [0-9]') do call "%curp%\%%b"

exit
