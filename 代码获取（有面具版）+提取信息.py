#-*-coding:utf-8-*-
import requests
import  re
import  sys
reload(sys)
sys.setdefaultencoding("gb18030")
type = sys.getfilesystemencoding()
#戴面具的情况
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers = headers)
#没戴面具的情况
#html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html.encoding = 'utf-8'
print html.text
#提取有用信息
text = re.findall(' alt=(.*?)</a>',html.text,re.S)
for each in text:
    print each


