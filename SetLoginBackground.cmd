@echo off
REM Expand variables at execution time instead of parse time
setlocal enabledelayedexpansion

REM Set path to folder of background images
REM Images must be less then 256KB, .jpg, and dimensions should match the screen resolution
set folder="C:\Users\%USERNAME%\Pictures\Login Backgrounds"
set target="C:\Windows\System32\oobe\info\Backgrounds\BackgroundDefault.jpg"

REM Choose random image
set count=0
for /r %folder% %%a in (*.jpg) do (
    set PICTURE_!count!=%%~a
    set /a count+=1
)

set /a x="%random% %% count"
set chosen=!PICTURE_%x%!

copy /y "%chosen%" %target%
