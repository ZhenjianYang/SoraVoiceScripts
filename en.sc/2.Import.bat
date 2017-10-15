@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

"%dir_tools%\SoraInputTalk.exe" -c p "%curp%\py"  "%tmp%\v.out.py" "%tmp%\v.py" "%tmp%\report_import.txt"