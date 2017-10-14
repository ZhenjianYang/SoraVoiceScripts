@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set pydir=%tmp%\v.py
set sndir=%tmp%\scena

mkdir "%sndir%"

for %%i in ("%pydir%\*.py") do (
title %curd% Compiling %%~ni
py "%%i" --cp=ms932 "--gp=%dir_sc%" "%sndir%"
)

