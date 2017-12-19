from http import cookiejar
from urllib import request,error
from urllib.parse import urlparse

class HtmlDownLoader(object):
	def download(self,url,retry_count=3,headers=None,proxy=None,data=None):
		if url is None:
			return None
		try:
			req=request.Request(url,headers=headers,data=data)
			cookie=cookiejar.CookieJar()
			cookie_process=request.HTTPCookieProcessor(cookie)
			opener=request.build_opener()
			if proxy:
				proxies={urlparse(url).scheme:proxy}
				opener.add_handler(request.ProxyHandler(proxies))
			content = opener.open(req).read()