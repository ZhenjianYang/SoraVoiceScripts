@echo off

set curp=%~dp0

for /f "delims=" %%b in ('dir /b "%curp%\*.bat" ^| findstr /b [0-9]') do call "%curp%\%%b"

exit
