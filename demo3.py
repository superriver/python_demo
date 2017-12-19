#coding=utf-8
import requests
import re
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#定义一个爬虫
class spider(object):
    def __init__(self):
        print("开始爬取内容")


    def getsource(self,url):
        html=requests.get(url)
        return html.text
    def changepage(self,url,total_page):
        now_page=int(re.search('index_(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page+1):
            link = re.sub('index_\d+','index_%s'%i,url,re.S)
            page_group.append(link)
        return page_group
    
