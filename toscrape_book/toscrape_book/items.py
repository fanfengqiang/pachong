# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeBookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price=scrapy.Field()
    review_rating= scrapy.Field()
    review_num= scrapy.Field()
    upc= scrapy.Field()
    stock= scrapy.Field()



    pass
