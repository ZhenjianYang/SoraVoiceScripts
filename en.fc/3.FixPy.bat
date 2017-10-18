@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set dirpy=%tmp%\v.py

"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\T0121.py" 1 "%dirpy%\T0121_1.py" 23
"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\T4121.py" 1 "%dirpy%\T4121_1.py" 17
"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\T4136.py" 1 "%dirpy%\T4136_1.py" 40
