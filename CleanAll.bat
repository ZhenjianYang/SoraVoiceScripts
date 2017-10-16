@echo off

cd %~dp0

for %%b in (cn.fc en.fc en.sc) do .\%%b\0.Clean.bat

