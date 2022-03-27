import ctypes
import os
import random
import sys
from distutils import command
from distutils.util import strtobool

import win32api
import win32con

# key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")


# 删除键值
# _winreg.DeleteValue(key, "IconUnderline")
import win32gui
import winnt
def Windows_img():
    path = r'./桌面壁纸'
    file = os.listdir(path)
    filepath = path + "/" + random.choice(file)
    zpath = os.path.abspath(filepath)
    # 读取注册表
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 在注册表中写入属性值
    win32api.RegSetValueEx(k, "wapaperStyle", 0, win32con.REG_SZ, "2")  # 0 代表桌面居中 2 代表拉伸桌面
    win32api.RegSetValueEx(k, "Tilewallpaper", 0, win32con.REG_SZ, "2")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, zpath, win32con.SPIF_SENDWININICHANGE)

if __name__ == '__main__':
    #Windows_img()
    path = r'./{}'.format(os.path.split(__file__)[-1])
    zpath = os.path.abspath(path).split('.')[0]+'.exe'
    print(zpath)

































    # # 创建新的键 newKey = win32api.RegCreateKeyEx(key, "MyNewkey") # 给新创建的键添加键值 win32api.RegSetValueEx(newKey,
    # "ValueName", win32con.REG_SZ, "ValueContent") ctypes.windll.shell32.ShellExecuteW(None, "runas",
    # sys.executable, __file__, None, 1) key = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE,
    # r"Software\Microsoft\Windows\CurrentVersion\Run", win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY |
    # win32con.KEY_ALL_ACCESS | win32con.KEY_WRITE)
    # key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
    #                             win32con.KEY_ALL_ACCESS)
    # # k = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
    # #                           win32con.KEY_ALL_ACCESS)
    # #win32api.RegSetValueEx(key, 'Test', 1, win32con.REG_SZ, 'testtesttest')
    # #print(win32api.RegQueryValueEx(key,'Test'))
    # # try:
    # #     print(win32api.RegDeleteValue(key, 'test'))
    # #     print(111)
    # # except:
    # #     pass
    # # print(111)
    #
    #
    # print(win32api.RegDeleteValue(key,'Test'))
    # path = r'./{}'.format(os.path.split(__file__)[-1])
    # zpath = os.path.abspath(path)
    # #path = os.path.realpath(__file__)
    # print(zpath.split('.')[0])

    # win32api.RegCreateKeyEx(k, "Test2", 0, winnt.REG_OPTION_CREATE_LINK, win32con.REG_SZ)
    # win32api.RegSetValueEx(k, "Test", 0, win32con.REG_SZ, "mysql")
    # win32api.RegCreateKey(key, 'Python')
    # win32api.RegSetValueEx(key, 'Version', 0, win32con.REG_SZ, '7.0.2900.2180')
    # print(os.path.realpath(__file__).split('.')[0])
