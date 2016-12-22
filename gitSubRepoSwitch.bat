rem @echo off
setlocal
cd %~dp0%
if "%1" NEQ "" cd %1
 
if exist __GIT goto hide

attrib -h ".git"
if exist ".git" goto show 

:hide
rename __GIT ".git"
attrib +h ".git"
goto end

:show
rename ".git" __GIT

:end
endlocal