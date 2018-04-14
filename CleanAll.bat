@echo off

cd %~dp0

for %%b in (cn.fc cn.sc en.fc en.sc en.3rd) do .\%%b\0.Clean.bat

