import scrapy

class PhoneSpider(scrapy.Spider):
	name='phone'
	allowed_domain=['product.suning.com']
	start_urls=[
	'https://product.suning.com/0000000000/181059980.html']

	def parse(self,response):
		