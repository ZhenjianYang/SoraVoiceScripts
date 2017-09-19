@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp.ori

title %curd% %~n0%

call "%curp%\..\Common.bat"

set tmp0=%curp%\tmp

xcopy /Q /Y /R "%tmp0%\scena" "%tmp%\scena\"


