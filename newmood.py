#!/usr/bin/python3.5
import requests
import re
import random
import subprocess
import os

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
    pattern3 = 'http://.*?jpg'   #匹配jpg图片下载地址的正则
    jpg_url = re.search(pattern3,r.text).group()
    print("Get "+jpg_url)
    wget_jpg = 'wget '+jpg_url+' -O a.jpg'
    print(wget_jpg)
    subprocess.run(wget_jpg,shell=True)
    path = os.getcwd()
    ch_wall = 'gsettings set org.gnome.desktop.background picture-uri '+'file://'+path+'/a.jpg'
    subprocess.run(ch_wall,shell=True)
    