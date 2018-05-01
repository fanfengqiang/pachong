# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class PriceConverterPipeline(object):

    exchange_rite=8.5309

    def process_item(self, item, spider):
        price=float(item['price'][1:])*self.exchange_rite

        item['price']='￥%.2f'%price

        return item

class BookPipeline(object):
    review_rating_map={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def process_item(self, item, spider):
        item['review_rating']=self.review_rating_map[item['review_rating']]

        return item
