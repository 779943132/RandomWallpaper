# RandomWallpaper
使用python写的一款桌面端的随机壁纸
# 如果想要使用可以直接下载dist目录下的程序
本软件是将网络上的图片下载下来，然后随机在下载图片里面抽取一张设置为壁纸
同时可以使用配置文件对壁纸切换时间，网络图片下载地址，本地图片存储数量进行修改
# 配置文件如下
```bash
#壁纸更换配置文件
#更换壁纸时间间隔
[时间]
time=10
#存储壁纸数量
[数量]
number=100
#是否开机自启,true自启动，false不自启动
[自启动]
autoStart=false
#壁纸下载源,如果需要可以无限追加
[外部壁纸链接]
;url1=https://api.btstu.cn/sjbz/?lx=m_meizi
;url2=https://api.btstu.cn/sjbz/?lx=m_dongman
;url3=https://tuapi.eees.cc/api.php?type=302&category=meinv
;url4=https://tuapi.eees.cc/api.php?type=302&category=dongman
;url5=https://tuapi.eees.cc/api.php?type=302&category=fengjing
url7=https://picsum.photos/2560/1440
```
如果想要二次打包，可以再修改代码后可以使用一下代码进行打包成exe文件
打包RandomWallpaper.pyw启动时会自动隐藏DOS窗口
```bash
pyinstaller -F -i 图标路径  代码路径
```
