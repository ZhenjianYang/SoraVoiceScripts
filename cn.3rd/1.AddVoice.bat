@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

"%dir_tools%\SoraInputVoiceId.exe" -ml "%curp%\out.py" "%curp%\out.msg" "%tmp%\v.out.py" "%tmp%\report_v.txt"