@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set py=%tmp%\py
md "%py%"

setlocal enabledelayedexpansion
for %%i in ("%curp%\py\*.py") do (
set a=%%~ni
for /f "tokens=1 delims=." %%j in ("!a!") do copy /Y "%%i" "%py%\%%j.py"
)

"%dir_tools%\SoraInputTalk.exe" -cw p "%py%"  "%tmp%\v.out.py" "%tmp%\v.py" "%tmp%\report_import.txt"