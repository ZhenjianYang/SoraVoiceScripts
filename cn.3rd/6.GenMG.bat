@echo off

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a
set tmp=%curp%\tmp

title %curd% %~n0%

call "%curp%\..\Common.bat"

set vqdir=%tmp%\v.mg.txt
set sndir=%tmp%\scena

mkdir "%sndir%"

for %%i in (%vqdir%\T_QUIZ*.txt) do py "%dir_tools%\Txt2Quiz.py" --cp=gbk "%%i" "%sndir%"
for %%i in (%vqdir%\T_FISH*.txt) do py "%dir_tools%\Txt2Fish.py" --cp=gbk "%dir_cn3rd%\%%~ni._DT" "%%i" "%sndir%"
for %%i in (%vqdir%\Z_POKER*.txt) do copy /Y "%%i" "%sndir%/%%~ni._DT"

