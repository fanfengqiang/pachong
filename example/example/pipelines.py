# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class PriceConverterPipeline(object):

    exchange_rite=8.5309

    def process_item(self, item, spider):
        price=float(item['price'][1:])*self.exchange_rite

        item['price_Y']='￥%.2f'%price

        return item
class DuplicatesPipeline(object):

    def __init__(self):
        self.book_set=set()

    def process_item(self,item,spideer):

        name=item['name']
        if name in self.book_set:
            raise DropItem("Duplicate book found:%s"%item)
        self.book_set.add(name)
        return item

        pass

    pass

