import configparser
import ctypes
import os
import random
import time
from distutils.util import strtobool

import win32gui

import regedit
import requests
from subprocess import run, PIPE

import win32api
import win32con
from fake_useragent import UserAgent

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')


if not os.path.exists('./桌面壁纸'):
    os.mkdir(r'./桌面壁纸')

#下载图片
def download_img(urls):
    headers = {
        'User-Agent': ua.random
    }

    url = urls[random.randint(0, len(urls) - 1)][1]
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    cur_time = time.strftime(format_time, time_tup) + '.jpg'
    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(r'./桌面壁纸/{}'.format(cur_time), 'wb') as f:
                f.write(response.content)
    except:
        pass
    
    path = r'./桌面壁纸'
    files = os.listdir(path)
    return len(files)


# 删除一半图片
def delete():
    path = r'./桌面壁纸'
    path = os.path.abspath(path)
    files = os.listdir(path)
    sample = random.sample(files, len(files) // 2)
    for each in sample:
        file_path = os.path.join(path, each)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except PermissionError as e:
            pass


# def set_wallpaper():
#     path = r'./桌面壁纸'
#     file = os.listdir(path)
#     filepath = path + "/" + random.choice(file)
#     filee = os.path.abspath(filepath)
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, filee, 0)

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


def create_config():
    # 创建配置文件
    if not os.path.isfile(r'./config.ini'):
        with open(r'./config.ini', 'w', encoding='GB18030') as f:
            configstr = '#壁纸更换配置文件\n' \
                        '\n' \
                        '#更换壁纸时间间隔\n' \
                        '[时间]\n' \
                        'time=30\n' \
                        '\n' \
                        '#存储壁纸数量\n' \
                        '[数量]\n' \
                        'number=500\n' \
                        '\n' \
                        '#是否开机自启,true自启动，false不自启动\n' \
                        '[自启动]\n' \
                        'autoStart=true\n' \
                        '\n' \
                        '#壁纸下载源,如果需要可以无限追加\n' \
                        '[外部壁纸链接]\n' \
                        'url1=https://api.btstu.cn/sjbz/?lx=m_meizi\n' \
                        'url2=https://api.btstu.cn/sjbz/?lx=m_dongman\n' \
                        'url3=https://tuapi.eees.cc/api.php?type=302&category=meinv\n' \
                        'url4=https://tuapi.eees.cc/api.php?type=302&category=dongman\n' \
                        'url5=https://tuapi.eees.cc/api.php?type=302&category=fengjing\n' \
                        'url6=https://tuapi.eees.cc/api.php?type=302&category=biying\n' \
                        '#url7=https://picsum.photos/2560/1440'
            f.write(configstr)
            f.close()


if __name__ == '__main__':
    # 创建配置文件
    create_config()
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read(r'./config.ini', encoding='GB18030')
    # 获取更新时间
    date = config.getint('时间', 'time')
    # 获取存储数量
    number = config.getint('数量', 'number')
    # 获取壁纸源
    urls = config.items('外部壁纸链接')

    # 是否自启动
    autoStart = strtobool(config.get('自启动', 'autoStart'))
    path = os.path.realpath(__file__).split('.')[0] + '.exe'
    if autoStart:
        regedit.set_regedit(path)
    else:
        regedit.del_regedit()

    # 判断是否有网
    while True:
        r = run('ping www.baidu.com', stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True)
        if r.returncode == 0:
            num = download_img(urls)
            # 如果壁纸数量达到设置的数目随机删除一半
            if num == number:
                delete()
        # 设置壁纸更换间隔
        time.sleep(date)
        # 设置壁纸
        #set_wallpaper()
        Windows_img()
