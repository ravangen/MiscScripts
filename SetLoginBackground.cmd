@echo off
setlocal enabledelayedexpansion

set folder="C:\Users\%username%\Pictures\Login Backgrounds"
set target="C:\Windows\System32\oobe\info\Backgrounds\BackgroundDefault.jpg"

set count=0
for /r %folder% %%a in (*.jpg) do (
	set PICTURE_!count!=%%~a
	set /a count+=1
)

set /a x="%random% %% count"
set chosen=!PICTURE_%x%!

copy /y "%chosen%" %target%
