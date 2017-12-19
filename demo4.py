#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
def crawl(url):
    header={'User-Agent':'Mozilla/5.0(Window;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Frefox/3.5.6'}
    req=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(req,timeout=20)
    contents=page.read()
    soup=BeautifulSoup(contents)
    my_girl=soup.findall('img')
    for girl in my_girl:
        link=girl.get('src')
        print(link)
        contents=urllib.request.urlopen(link).read()
        with open(u'D:/meizi'+'/'+link[-11:],'wb') as code:
            code.write(contents)


if __name__=='__main__':
    page_start=0
    page_end=10
    for page in range(page_start,page_end):
        page+=1
        url='http://www.dbmeinv.com/?pager_offset=%s'%page
        crawl(url)

    print("success");
