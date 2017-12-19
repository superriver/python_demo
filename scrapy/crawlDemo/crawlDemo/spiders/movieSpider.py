from scrapy.spiders import CrawlSpider,Rule,Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from crawlDemo.items import MoviceItem
from scrapy.selector import Selector
class MoiveSpider(CrawlSpider):
	"""docstring for ClassName"""
	name = 'moive'
	allowed_domains = ['movie.douban.com']
	start_urls=[
	'http://movie.douban.com/top250'
	]
	rules=[
		Rule(LxmlLinkExtractor(allow=(r'\?start = \d+.*'))),
		Rule(LxmlLinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback = 'parse_item',follow = True)
	]
	def parse_item(self, response):
		sel = Selector(response)
		item = MoviceItem()
		item['name'] = sel.xpath("//*div[@id='content']/h1/span[1]/text()").extract()
		item['year'] = sel.xpath("//*[@id='content']/h1/span[2]/text()").re(r'\((\d+)\)')
		item['score'] = sel.xpath("//*div[@class='clearfix']/strong/text()").extract()
		item['director'] = sel.xpath("//*div[@id='info']/span[1]/a/text()").extract()
		item['classification'] = sel.xpath("//span[@property='v:genre']/text()").extract()
		item['actor'] = sel.xpath("//*span[@class='actor']//a/text()").extract()
		return item
