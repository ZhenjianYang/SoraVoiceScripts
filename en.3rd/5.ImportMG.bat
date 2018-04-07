@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set vtxtdir=%tmp%\v.mg.txt
set txtdir=%curp%\mg.txt
set evodir=%curp%\mg.txt.evo

"%dir_tools%\SoraInputVoiceId.exe" -sm "%txtdir%" "%evodir%" "%vtxtdir%" ""
