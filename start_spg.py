import win32api
import win32con



win32api.keybd_event(17,0,0,0)
win32api.keybd_event(83,0,0,0)
win32api.keybd_event(80,0,0,0)
win32api.keybd_event(71,0,0,0)
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0)#
win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0)
