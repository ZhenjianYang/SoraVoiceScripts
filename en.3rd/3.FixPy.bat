@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set dirpy=%tmp%\v.py

"%dir_tools%\SoraMoveFuns.exe" 0 "%dirpy%\T4206.py" 1 "%dirpy%\T4206_1.py" 17
"%dir_tools%\SoraMoveFuns.exe" 1 "%dirpy%\U7000_1.py" 0 "%dirpy%\U7000.py" 38
"%dir_tools%\SoraMoveFuns.exe" 2 "%dirpy%\U7000_2.py" 0 "%dirpy%\U7000.py" 13
"%dir_tools%\SoraMoveFuns.exe" 3 "%dirpy%\U7000_3.py" 0 "%dirpy%\U7000.py" 17

