#-*coding:utf-8-*-
import requests
html = requests.get('http://www.jikexueyuan.com/path/python/')
print html.text