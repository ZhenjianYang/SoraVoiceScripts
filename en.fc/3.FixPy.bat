@echo off
title %~n0%

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

call "%curp%\..\Common.bat"

set dirpy=%tmp%\v.py

"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\T4136.py" "%dirpy%\T4136_1.py" 9
"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\T4121.py" "%dirpy%\T4121_1.py" 5
"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\T0121.py" "%dirpy%\T0121_1.py" 2