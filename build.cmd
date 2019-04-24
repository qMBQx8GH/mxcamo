SETLOCAL ENABLEDELAYEDEXPANSION

SET GAME_FOLDER=
SET INI=build.ini
set area=[Game]
set key=folder
set currarea=
for /f "usebackq delims=" %%a in ("!INI!") do (
    set ln=%%a
    if "x!ln:~0,1!"=="x[" (
        set currarea=!ln!
    ) else (
        for /f "tokens=1,2 delims==" %%b in ("!ln!") do (
            set currkey=%%b
            set currval=%%c
            if "x!area!"=="x!currarea!" if "x!key!"=="x!currkey!" (
                set GAME_FOLDER=%%c
            )
        )
    )
)
echo %GAME_FOLDER%

set DESTINATION=
set area=[Destination]
set key=folder
set currarea=
for /f "usebackq delims=" %%a in ("!INI!") do (
    set ln=%%a
    if "x!ln:~0,1!"=="x[" (
        set currarea=!ln!
    ) else (
        for /f "tokens=1,2 delims==" %%b in ("!ln!") do (
            set currkey=%%b
            set currval=%%c
            if "x!area!"=="x!currarea!" if "x!key!"=="x!currkey!" (
                set DESTINATION=%%c
            )
        )
    )
)
echo %GAME_FOLDER%

SET REV=
for /f "tokens=*" %%i in ('hg parent --template "{rev}"') do (
  set REV=%%i
)
echo %REV%

set PATHS=
for /f "tokens=3 delims=/" %%i in ('findstr /r "<Path>../res_mods" %GAME_FOLDER%\bin64\paths.xml') do (
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
"C:\Program Files\7-Zip\7z.exe" a -r %DESTINATION%\mxcamo-%VERS%-%REV%.zip %VER%
