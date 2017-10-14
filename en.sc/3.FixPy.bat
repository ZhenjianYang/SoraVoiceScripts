@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set dirpy=%tmp%\v.py

"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\E0310.py" "%dirpy%\E0310_1.py" 2
"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\T2120.py" "%dirpy%\T2120_1.py" 7
"%dir_tools%\SoraMoveFuns.exe" "%dirpy%\T2132_1.py" "%dirpy%\T2132_2.py" 20 2