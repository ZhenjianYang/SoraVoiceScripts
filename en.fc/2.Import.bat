@echo off
title %~n0%

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

call "%curp%\..\Common.bat"

"%dir_tools%\SoraInputTalk.exe" -c p "%curp%\py"  "%tmp%\v.out.py" "%tmp%\v.py" "%tmp%\report_import.txt"