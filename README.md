# X11-in-Python3.9-Windows10
Quick guide to setting up X-11 (VcXsrv) on Windows 10.


Pre-requisites
=
```
* Windows 10
* VcXsrv       (1.20.9.0) 
* Python       (3.9.6)
* PIP          (23.3)
* python-xlib  (0.31)
```

Install VcXsrv X Server
=
https://sourceforge.net/projects/vcxsrv/
```
X-11 server for Windows 10
As of project date, Version 1.20.9.0 (Jan 3. 2021)
```



 
(Optional) Install the latest PIP
=
```
python.exe -m pip install --upgrade pip
```



Install python-xlib
=
```
python.exe -m pip install python-xlib


Installing collected packages: python-xlib
Successfully installed python-xlib-0.31
```

Run x11test.py
=
```
C:\X11-in-Pthon3.9-Windows10\python.exe x11text.py
```

```
fcntl.py is a workaround for Windows 10, for the following errors: 
ModuleNotFoundError: No module named 'fcntl'
```

