from bs4 import BeautifulSoup
import os
import urllib.request

def urlBs(url):
	response=urllib.request.urlopen(url)
	html=response.read()
	soup = BeautifulSoup(html)
	return soup

def main(url):
	try:
		soup = urlBs(url)
		links = soup.select('.booklist a')
		path = os.getcwd()+u"/读者文章/"
		if not os.path.isdir(path):
			os.makedirs(path)
		for item in links:
			newsUrl = baseUrl+item['href'];
			result = urlBs(newsUrl)
			title = result.find('h1').string
			author = result.find(id='pub_date').string.strip()
			fileName = path+title+'.txt'
			article = open(fileName,"w")
			article.write("<<"+title+">>\n\n")
			article.write(author+"\n\n")
			text = result.select('.blkContainerSblkCon p')
			for p in text:
				content = p.text
				article.write(content)

	except Exception as e:
		raise
	else:
		pass
	finally:
		article.close()


if __name__ == '__main__':
	baseUrl = "https://yd.baidu.com/view/55c96ffb112de2bd960590c69ec3d5bbfc0ada42?cn=1-1,2-1"
	mainbaseUrl 
	
