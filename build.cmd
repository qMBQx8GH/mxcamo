rmdir /s /q dist 
mkdir dist
cd dist
mkdir %1
cd %1
echo >PnFModsLoader.py
mkdir PnFMods
xcopy ..\..\HelpMe PnFMods\HelpMe /i /e
echo dir=%3 >PnFMods\HelpMe\helpme.ini
cd ..
"C:\Program Files\7-Zip\7z.exe" a -r C:\src\owncloud\HelpMe\helpme-%1-%2-%3.zip %1
cd ..
