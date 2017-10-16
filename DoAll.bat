@echo off

cd %~dp0

for %%b in (cn.fc en.fc en.sc) do start .\%%b\DoAll.bat

exit