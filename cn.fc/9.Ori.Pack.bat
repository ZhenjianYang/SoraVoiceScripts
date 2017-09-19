@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp.ori

title %curd% %~n0%

call "%curp%\..\Common.bat"

set sndir=%tmp%\scena
set outdir=%curp%\..\pack\%dt%

md "%outdir%"

"%Zip7%" -t7z -mx=9 a "%outdir%\%curd%.ori_%dt%.7z" "%sndir%"
