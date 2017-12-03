import urllib
import crawl
import time
import re
import urllib.parse
import ssl
from dataman import *
from multiprocessing  import Process,Queue 
import multiprocessing
import sys
import pybloom_live
import processmanage
           
def downloadhtml(pro_num):
    i=0
    url_current=[]
    while 1:
        if not url_next_num.empty():
            num_current=str(url_next_num.get())
            while 1:
                try:
                    data1=crawl.download('https://www.tianyancha.com/company/'+num_current)  #下载数据进行bs编码，返回bs编码后的数据
                except Exception:
                    print('出现错误了!')
                    time.sleep(2)
                    continue                    #如果出现错误，则进行下一次循环
                else:
                    break                       #如果没有出现错误，则跳出循环继续执行
                
               
      
            save=dataoperate(str(data1),num_current) #储存器模块
            if  i!=0:
                save.data_save()                 #存入当前网页数据，为txt文档(第一圈不保存)
                save.url_save()                  #存入已经爬过的当前url，为txt文档
            #time.sleep(3)    

            url_current=crawl.url_get(data1)    #获取当前页面所有包含公司的url编号，返回去重后的编号列表
            for num1 in url_current:
                url_current_num.put(num1)       #压入队列
            i=i+1
            print('爬虫进程%d运行了%d次'%(pro_num,i))        




def queue_arrange():
    m=0
    url_total=[]
    url_total=list_open.url_list_read()
    url_next_num.put(url_total[len(url_total)-1])
    b =pybloom_live.BloomFilter(capacity=90000000,error_rate=0.01)
    with open('urllist.txt','r') as file_object:
        for line in file_object:
            b.add(line.rstrip()) 
    while 1:
        try:
            url_current=[]
            if  not url_current_num.empty():         #对url_total队列进行去重，并将url_current_num压入总列表和队列
                while not url_current_num.empty():                   
                     url_current.append(url_current_num.get())
            
                for num1 in url_current:
                    if num1 not in b:
                           #url_total.append(num1)          
                           url_next_num.put(num1)
                           b.add(str(num1))
                m=m+1
                print('url管理进程运行了%d次'%(m))
                print('total列表有%d个元素'%(len(url_total)))
                #b.sync()
                #time.sleep(2)
        except Exception:
            continue
def manage(proc):
    while 1:
        time.sleep(5)
        print(len(proc))
        i=0
        for proce in proc:
            print('process%d:'%(i))
            print(proce.is_alive())
            i=i+1
if __name__=='__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    sys.setrecursionlimit(999999999)

    print("请输入爬虫进程个数，按回车开始")       #起始页

    pachong_num=int(input())
    url_current_num=Queue()
    url_next_num=Queue()
    htmldata=Queue()
    list_open=dataoperate(None,None)
    p=[]
    pro=[]
    i=0
    while i<pachong_num:    
        pro.append(multiprocessing.Process(target=downloadhtml,args=(i,)))
        pro[i].start()
        i=i+1
    pro.append(multiprocessing.Process(target=queue_arrange))
    pro[i].start()
   
    processmanage.manage(pro)
    
        
    
    


   
                                    

