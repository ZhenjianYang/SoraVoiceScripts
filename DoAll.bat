@echo off

cd %~dp0

for %%b in (cn.fc en.fc en.sc en.3rd) do start .\%%b\DoAll.bat

exit