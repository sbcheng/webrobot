import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def download(url):
    #url=urllib.parse.urlencode(url)
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers={'Host':'chengdou.tianyancha.com:443',
    'Proxy-Connection':'keep-alive',
    'User-Agent':'user_agent'}
    req=urllib.request.Request(url,None,headers)
    word=urllib.request.urlopen(req).read()
    
    word_e=BeautifulSoup(word,"lxml")
    word_d=word.decode('utf-8')
    return word_e

def url_get(data1):
    data2_url=data1.find_all(href=re.compile('/company/([0-9]{5,11})'))  #取得该页面所有关于公司的url
    #data2_url=data1.find_all('a',attrs={'href':'/company/'})                    #取得所有属性为author的标签
    url_current=[]
    data3_url=[] 
    i=0
    for content in data2_url:
        content=str(content)        
        data3_url.append(re.search(re.compile('/company/([0-9]{5,11})'),content)) #将公司代码过滤加入列表
        url_current.append(str(data3_url[i].group(1)))                                #将公司代码加入当前页面代码列表
        print(data3_url[i])
        print(url_current[i])
        i=i+1
        print('第%d个url'%(i))
    url_current=list(set(url_current))
    return(url_current)
        

#def next_page(word_e):                               #查找下一页网址
    nexturl=re.search(re.compile('nextid=(.+?)"'),str(word_e))
    return nexturl


    
    
