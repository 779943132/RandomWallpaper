import os

import win32api
import win32con


def set_regedit(path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                              win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(k, 'RandomWallpaper', 1, win32con.REG_SZ, path)
    win32api.RegCloseKey(k)


def del_regedit():
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                              win32con.KEY_ALL_ACCESS)

    try:
        win32api.RegDeleteValue(key, 'RandomWallpaper')
    except:
        pass
