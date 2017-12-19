import pymongo
from scrapy.exceptions import  DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):
	"""docstring for MongoDBPipeline"""
	def __init__(self, arg):
		self.connection = pymongo.Connection(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
		self.db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTIONI']]

	def process_item(self,item,spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing %s of blogpost from %s"%(data,item['url']))
			if valid:
				new_moive = [{
				"name":item['name'][0],
				"year":item['year'][0],
				"score":item['score'][0],
				"director":item['director'],
				"classification":item['classification'],
				"actor":item['actor']
				}]
				self.collection.insert(new_moive)
				log.msg("item wrote to MongoDB database %s/%s"%
					(settings['MONGODB_DB'],settings['MONGODB_COLLECTIONI']),
					level = log.DEBUG,spider = spider)
			return item