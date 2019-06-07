import requests
import re
import random
import os
import win32api
import win32con
import win32gui
from PIL import Image

if __name__ == '__main__':
    #del_jpg="rm a.jpg" 
    #subprocess.run(del_jpg,shell=True)
    url1 = url2 = 'https://bing.ioliu.cn' #必应壁纸url
    pattern1 = '<a class=\"mark\" href=\"[^\"]*' #匹配壁纸url的正则1
    pattern2 = '/.*' #匹配壁纸url的正则2
    print("Get "+url1)
    r = requests.get(url1)
    results = re.findall(pattern1,r.text)
    url2 += re.search(pattern2,results[random.randint(0,len(results)-1)]).group()
    print("Get "+url2)
    r = requests.get(url2)
    #pattern3 = 'http://.*?jpg'  
    pattern3 = 'https://h1.ioliu.cn//bing/.*?jpg' #匹配jpg图片下载地址的正则
    jpg_url = re.search(pattern3,r.text).group()
    print("Get "+jpg_url)
    response = requests.get(jpg_url)
    print("Finish")
    jpgFile = 'a.jpg'
    bmpFile = os.getcwd()+'\\a.bmp'
    with open(jpgFile,'wb') as file:
        file.write(response.content)
    img = Image.open(jpgFile)
    img.save(bmpFile,'BMP')
    os.remove(jpgFile)
    print("Setting the image as background")
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmpFile, 1+2)
