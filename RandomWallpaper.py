import configparser
import ctypes
import os
import random
import time
import urllib
import urllib.request
from distutils.util import strtobool
from subprocess import run, PIPE

import win32api
import win32gui
from fake_useragent import UserAgent

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
if not os.path.exists('./桌面壁纸'):
    os.mkdir(r'./桌面壁纸')


def download_img(urls):
    headers = {
        'User-Agent': ua.random
    }

    url = urls[random.randint(0, len(urls) - 1)][1]

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    # print(response.getcode())  # 返回状态码

    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    cur_time = time.strftime(format_time, time_tup) + '.jpg'

    if response.getcode() == 200:
        with open(r'./桌面壁纸/{}'.format(cur_time), "wb") as f:
            f.write(response.read())
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


def set_wallpaper():
    path = r'./桌面壁纸'
    file = os.listdir(path)
    filepath = path + "/" + random.choice(file)
    filee = os.path.abspath(filepath)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filee, 0)


def create_config():
    # 创建配置文件
    if not os.path.isfile(r'./config.ini'):
        with open(r'./config.ini', 'w', encoding='GB18030') as f:
            configstr = '#壁纸更换配置文件\n' \
                        '\n' \
                        '#更换壁纸时间间隔\n' \
                        '[时间]\n' \
                        'time=10\n' \
                        '\n' \
                        '#存储壁纸数量\n' \
                        '[数量]\n' \
                        'number=100\n' \
                        '\n' \
                        '#如果需要开机自启动，将软件创建快捷方式放入以下目录即可\n' \
                        '#C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp\n' \
                        '\n' \
                        '#壁纸下载源,如果需要可以无限追加\n' \
                        '[外部壁纸链接]\n' \
                        'url1=https://api.btstu.cn/sjbz/?lx=m_meizi\n' \
                        'url2=https://api.btstu.cn/sjbz/?lx=m_dongman\n' \
                        'url3=https://tuapi.eees.cc/api.php?type=302&category=meinv\n' \
                        'url4=https://tuapi.eees.cc/api.php?type=302&category=dongman\n' \
                        'url5=https://tuapi.eees.cc/api.php?type=302&category=fengjing'
            f.write(configstr)
            f.close()

    # '#是否开机自启,true自启动，false不自启动\n' \
    # '[自启动]\n' \
    # 'autoStart=false\n' \


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
    # autoStart = strtobool(config.get('自启动', 'autoStart'))

    # 隐藏命令窗
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
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
        set_wallpaper()
