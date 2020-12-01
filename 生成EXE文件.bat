pyinstaller -Fw  -i order_162.ico ZionOrder.py
pyinstaller -Fw  -i order_162.ico GraficaCedarOrder.py
pyinstaller -Fw  -i order_162.ico ColorProOrder.py
ren dist\ZionOrder.exe    ZionOrder"%date:~0,4%
%date:~5,2%%date:~8,2%".exe
ren dist\GraficaCedarOrder.exe    GraficaCedarOrder%date:~0,4%
%date:~5,2%%date:~8,2%.exe
ren dist\ColorProOrder.exe    ColorProOrder%date:~0,4%
%date:~5,2%%date:~8,2%.exe
