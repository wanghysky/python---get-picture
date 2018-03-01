# -*- coding: utf-8 -*
from urllib import request  
from  bs4 import BeautifulSoup  
import re  
import time  
import os
import os.path
from PIL import Image
import shutil  
import os  
  
  
def changePC(page):
    global named 
    global names 
    url = "http://www.jianai360.com/search.html?photo=1&p="+str(page)  
    html = request.urlopen(url).read().decode('utf-8')  
    soup = BeautifulSoup(html,'html.parser')  
    links = soup.find_all('a', "ja_s_pic",target=re.compile(r'_blank'))
    
    for link in links:
        page1 = link.attrs['href']
#        print(page1)
        html1 = request.urlopen(page1).read().decode('utf-8')
        soup1 = BeautifulSoup(html1,'html.parser')
        headers = soup1.find_all('img', 'cpic' ,src=re.compile(r'.jpg?'))
        for header in headers:
            path1 = r'D:\picture\head'                            #路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义
#           print(header.attrs['src'])
            request.urlretrieve(header.attrs['src'],path1+'\%d.jpg' % named)
#            Resizehead()
            named +=1
#        pictures2 = soup1.find_all('img',width=r'60',src=re.compile(r'.jpg'))
        pictures = soup1.find_all('div',attrs={'class':"c_plist"})
        for picture in pictures:
            imagenations = picture.find_all('a')
            for imagenation in imagenations:
                path2 = r'D:\picture\image'
                naming = str(named-1)+'TT'+str(names)
                request.urlretrieve(imagenation.attrs['href'],path2+'\%s.jpg' % naming)  #使用request.urlretrieve直接将所有远程链接数据下载到本地  
#                ResizeImage()
                names += 1
def Resizehead():
    global named 
    img = Image.open('D:\\picture\\head\\'+str(named)+'.jpg')
    out = img.resize((298, 297),Image.ANTIALIAS) #resize image with high-quality
    out.save('D:\\picture\\head\\'+str(named)+'.jpg')

def ResizeImage():
    global names 
    global named 
    naming = str(named-1)+'TT'+str(names)
    img = Image.open('D:\\picture\\image\\'+naming+'.jpg')
    out = img.resize((382, 611),Image.ANTIALIAS) #resize image with high-quality
    out.save('D:\\picture\\image\\'+naming+'.jpg')
  
i=0
global named
global names
named = 0
names = 0
for i in range(0,25):
   changePC(i)