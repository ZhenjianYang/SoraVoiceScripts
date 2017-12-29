@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set vqdir=%tmp%\v.quiz.txt
set sndir=%tmp%\scena

mkdir "%sndir%"

for %%i in (%vqdir%\*.txt) do py "%dir_tools%\Txt2Quiz.py" --cp=ms932 "%%i" "%sndir%"

