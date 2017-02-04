echo "do cleaning before build..."
del/f/s/q ..\bin\nbarecord.exe
rd/s/q build
del/f/s/q nbarecord.spec
echo "start to build..."
pyinstaller.exe --onefile --distpath bin --console getrecord.py --name=nbarecord --clean
echo "build finished."
echo "start to clean..."
rd/s/q build
del/f/s/q nbarecord.spec
echo "clean finished."
pause

