SETLOCAL ENABLEDELAYEDEXPANSION

SET REV=
for /f "tokens=*" %%i in ('hg parent --template "{rev}"') do (
  set REV=%%i
)
echo %REV%

set PATHS=
for /f "tokens=2 delims=/" %%i in ('findstr /r "<Path>res_mods" C:\games\World_of_Warships\paths.xml') do (
  set PATHS=%%i
)
SET VERS=%PATHS:~0,-1%
echo %VERS%

rmdir /s /q dist 
mkdir dist
cd dist
mkdir %VERS%
cd %VERS%
xcopy ..\..\out\gui gui /i /e
cd ..
"C:\Program Files\7-Zip\7z.exe" a -r C:\src\owncloud\mxcamo\mxcamo-%VERS%-%REV%.zip %VER%
