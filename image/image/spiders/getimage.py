# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request


class GetimageSpider(scrapy.Spider):
    name = 'getimage'

    BASE_URL='http://image.so.com/j?q=%E6%9D%A8%E5%B9%82&src=srp&correct=%E6%9D%A8%E5%B9%82&pn=60&ch=&sn={}&sid={}&ran=0&ras=0&cn=0&gn=10&kn=50'
           # 'http://image.so.com/j?q=%E6%9D%A8%E5%B9%82&src=srp&correct=%E6%9D%A8%E5%B9%82&pn=60&ch=&sn=240&sid={1}&ran=0&ras=0&cn=0&gn=10&kn=50'
    start_urls = [BASE_URL.format('120','4523bfb1b8e4f5532673deb02cbcb6e2')]
    start_index=0
    def parse(self, response):
        jslist=json.loads(response.body.decode('utf-8'))
        #a=jslist['list']
        # for i in range(len(jslist['list'])):
        #     yield {'image_urls':jslist['list'][i]['img']}
        yield {'image_urls':[info['thumb_bak'] for info in jslist['list']]}
        #yield {'image_urls':[jslist['list'][i]['img'] for i in range(len(jslist['list']))]}



        self.start_index+=60
        sid=jslist['sid']
        if sid and self.start_index<100000:
            yield Request(self.BASE_URL.format(self.start_index,sid))
        pass
