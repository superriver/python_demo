
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.lxmlhtml import  LxmlLinkExtractor
from crawlDemo.items import CrawldemoItem

class Csdnspider(CrawlSpider):
	name = 'csdn'
	allowed_domain=['blog.csdn.net']
	start_urls=[
		'http://blog.csdn.net/hjjdehao/article/list'
	]
#http://blog.csdn.net/hjjdehao/article/list/2
	rules=[
		Rule(LxmlLinkExtractor(allow=(r'/hjjdehao/article/list/.*',)),callback='parse_next_page'),
	]
			

	def parse_next_page(self,response):
		for sel in response.xpath('//div[@id="hotarticls"]/ul/li'):
			item=CrawldemoItem()
			item['title']=sel.xpath("a/text()").extract()
			item['link']= sel.xpath("a/@href").extract()
			yield item
		# item=CrawldemoItem()
		# item['title']=response.xpath("//ul[@class='itemlist']/li/a/text()").extract()
		# item['link']= response.xpath("//ul[@class='itemlist']/li/a/@href").extract()
		# return item
		# with open('response','wb') as file:
		# 	 file.write(response.body)
