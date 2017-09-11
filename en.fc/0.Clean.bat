@echo off
title %~n0%

set curp=%~dp0
set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

rd /S /Q "%curp%\tmp"
