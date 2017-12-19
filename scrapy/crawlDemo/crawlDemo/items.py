# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
  	url = scrapy.Field()
  	title = scrapy.Field()
  	print("CrawldemoItem->",url,title)

class MoviceItem(scrapy.Item):
	"""docstring for ClassName"""
	name = scrapy.Field()
	year = scrapy.Field()
	score = scrapy.Field()
	director = scrapy.Field()
	classification = scrapy.Field()
	actor = scrapy.Field()
	pass