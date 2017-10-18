@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set dirpy=%tmp%\v.py

"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\E0310.py" 1 "%dirpy%\E0310_1.py" 38
"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\T2120.py" 1 "%dirpy%\T2120_1.py" 19
"%dir_tools%\SoraMoveFuns.exe" 1 "%dirpy%\T2132_1.py" 0 "%dirpy%\T2132.py" 25
