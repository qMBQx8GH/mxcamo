C:\Python36\python make_icons.py
rmdir /s /q dist 
mkdir dist
cd dist
mkdir %1
cd %1
xcopy ..\..\out\gui gui /i /e
cd ..
"C:\Program Files\7-Zip\7z.exe" a -r C:\src\owncloud\mxcamo\mxcamo-%1-%2.zip %1
