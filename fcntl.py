def F_SETFD():
    return
def fcntl(fd, op, arg=0):
    return 0
    
"""
def ioctl(fd, op, arg=0, mutable_flag=True):
    if mutable_flag:
        return 0
    else:
        return ""

def flock(fd, op):
    return
        
def lockf(fd, operation, length=0, start=0, whence=0):
    return
"""

# fcntl.py is a workaround for the following error(s):

# ModuleNotFoundError: No module named 'FCNTL'

#Traceback (most recent call last):
#  File "C:\X11-in-Python3.9-Windows10\x11test.py", line 34, in <module>
#    Window(display.Display("localhost:0.0"), "Hello, World!").loop()
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\display.py", line 89, in __init__
#    self.display = _BaseDisplay(display)
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\display.py", line 71, in __init__
#    protocol_display.Display.__init__(self, *args, **keys)
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\protocol\display.py", line 84, in __init__
#    name, protocol, host, displayno, screenno = connect.get_display(display)
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\support\connect.py", line 72, in get_display
#    mod = _relative_import(modname)
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\support\connect.py", line 55, in _relative_import
#    return importlib.import_module('..' + modname, __name__)
#  File "C:\Users\x\Python39\lib\importlib\__init__.py", line 127, in import_module
#    return _bootstrap._gcd_import(name[level:], package, level)
#  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
#  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
#  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
#  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
#  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
#  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
#  File "C:\Users\x\Python39\lib\site-packages\Xlib\support\unix_connect.py", line 40, in <module>
#    from FCNTL import F_SETFD, FD_CLOEXEC
# ModuleNotFoundError: No module named 'FCNTL
