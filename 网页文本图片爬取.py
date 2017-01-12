#-*- coding:utf-8 -*-
import re
import requests
f =open('sourse.txt','r')
#死胡同！！！有中文无法正确解码
html = f.read()
f.close()

#匹配图片网址 ??pic_url的list是空的？？？答：代码中小心空格
pic_url=re.findall('img src="(.*?)" class="lessonimg"',html,re.S)
i=0
print(pic_url)
for each in pic_url:
    print('now downloading:' +each)
    pic=requests.get(each)
    fp=open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1