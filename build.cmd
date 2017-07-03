rmdir /s /q dist 
mkdir dist
cd dist
mkdir %1
cd %1
echo >PnFModsLoader.py
mkdir PnFMods
xcopy ..\..\HelpMe PnFMods\HelpMe /i
cd ..
"C:\Program Files\7-Zip\7z.exe" a -r C:\src\owncloud\HelpMe\%1-%2.zip %1
