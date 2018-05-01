# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name=Field()
    price=Field()
    price_Y=Field()


    pass
