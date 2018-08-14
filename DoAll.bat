@echo off

cd %~dp0

for %%b in (cn.fc cn.sc cn.3rd en.fc en.sc en.3rd) do start .\%%b\DoAll.bat

exit