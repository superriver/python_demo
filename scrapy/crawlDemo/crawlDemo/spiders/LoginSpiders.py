import scrapy
from scrapy.spiders import CrawlSpider,Rule
from  scrapy.http import FormRequest,Request
from scrapy.selector import Selector

class LoginSpiders(CrawlSpider):
	name = "LoginSpiders"
	allowed_domains=['passport.csdn.net']
	start_urls=['https://passport.csdn.net/']
	loginUrl = "https://passport.csdn.net/account/verify"
	LoginCheckUrl= 'https://passport.csdn.net/account/verify;jsessionid=465D05CB2EC553AC4ECFF846C1A15B59.tomcat1'

	header = {
        # 使用手机的User-Agent
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'Host': 'passport.csdn.net',
        "Referer": "https://passport.csdn.net/",
    }

	def start_requests(self):
		return [scrapy.Request(
			url= self.loginUrl,
			meta = {'cookiejar':1},
			headers = self.header,
			callback=self.post_login
			)]

	def post_login(self,response):
		lt = response.xpath("//input[@name='lt']/@value").extract()
		execs = response.xpath("//input[@name='execution']/@value").extract()
		eventId = response.xpath("//input[@name='_eventId']/@value").extract()
		print("response--"+str(execs))
		formdata={
		"username":"2521639848@qq.com1",
		"password":"huang.river",
		"lt":lt,
		"execution":execs,
		"_eventId":eventId
			}
		return [scrapy.FormRequest.from_response(response,
			url=self.LoginCheckUrl,
			meta={'cookiejar':response.meta['cookiejar']},
			formdata = formdata,
			callback=self.after_login,
			method='POST')]

	def after_login(self,response):
		print("登录成功！")
		# for u in self.start_urls:
		# 	yield scrapy.Request(url=u,
		# 		meta = {'cookiejar':response.meta['cookiejar']},
		# 			callback = self.parse)