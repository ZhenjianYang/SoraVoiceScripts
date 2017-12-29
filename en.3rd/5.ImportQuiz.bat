@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set vtxtdir=%tmp%\v.quiz.txt
set txtdir=%curp%\quiz.txt
set evodir=%curp%\quiz.txt.evo

"%dir_tools%\SoraInputVoiceId.exe" -sm "%txtdir%" "%evodir%" "%vtxtdir%" ""
