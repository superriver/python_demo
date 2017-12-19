#coding:utf-8
from bs4 import BeautifulSoup
import time,re,urllib.request
t=time.time()
websiteurls={}
def scanpage(url):
    websiteurl = url
    t = time.time()
    n=0
    html=urllib.request.urlopen(websiteurl).read()
    soup=BeautifulSoup(html,"html.parser")
    pageurls={}
    Upageurls={}
    pageurls=soup.find_all("a",href=True)
    for links in pageurls:
        if websiteurl in links.get("href") and links.get("href") not in Upageurls and links.get("href") not in websiteurls:
            Upageurls[links.get("href")]=0
    for links in Upageurls.keys():
        try:
            urllib.request.urlopen(links).getcode()
        except:
            print("connect failed")
        else:
            t2=time.time()
            Upageurls[links]=urllib.request.urlopen(links).getcode()
            print(n,links,Upageurls[links])
        n+=1
    print("total is "+repr(n)+"links")
    print(time.time()-t)

scanpage("http://news.163.com/")                                                         
                                                        
