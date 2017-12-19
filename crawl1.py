#coding:utf-8

from bs4 import BeautifulSoup
import os
import urllib.request

def getSoup(url):
	response =urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

urls = set()

fileObj = open('世界顶级思维.txt','a',encoding='utf-8')

def main(url):

	global new_url_end
	try:
		soup = getSoup(url)
	# new_soup = soup.prettify().replace(u'\xa0', '')
	# s_soup = BeautifulSoup(new_soup, 'html.parser')  # 再次将其转为bs4格式数据
 #    cont = s_soup.p.encode('gb18030')   # print type(cont)返回 <type 'str'>
 #    print(cont)

		
		title = soup.select('.catHead p')
		for p in title:
			print(p.text)
			fileObj.write(p.text)
		fileObj.write('\n')
		text = soup.select('.r_c p')
		for p in text:
			fileObj.write(p.text)
		fileObj.write('\n')
		nextArticle = soup.select('.p_n a')
		for p in nextArticle:
			url_end = p['href']

			if 'pn' not in url_end:
				new_url_end = url_end+'&pn=1'
			else:
				new_url_end = url_end
			new_url = baseUrl+new_url_end	
			if new_url not in urls:
				urls.add(new_url)
				print("--"+new_url)
				main(new_url)
	except Exception as e:
		raise e
	finally:
		fileObj.close()
		
if __name__ == '__main__':
	url_end = "?cn=1-1,2-1&pn=1"
	baseUrl = "https://yd.baidu.com/view/55c96ffb112de2bd960590c69ec3d5bbfc0ada42"
	firstUrl = baseUrl+url_end
	urls.add(firstUrl)
	main(firstUrl)
