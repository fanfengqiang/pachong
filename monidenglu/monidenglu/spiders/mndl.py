# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
from ..items import MonidengluItem


class MndlSpider(scrapy.Spider):
    name = 'mndl'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile']

    def parse(self, response):
        item=MonidengluItem()

        item['keys']=response.xpath('//*[@id="auth_user_first_name__label"]/text()').re_first('(.+):')
        item['values']=response.css('#auth_user_first_name__row > td:nth-child(2)::text').extract_first()
        yield item
    login_url='http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
    def start_requests(self):
        yield Request(self.login_url,callback=self.login)
    def login(self, response):
        df={'email':'liushuo@webscraping.com','password':'12345678'}
        yield FormRequest.from_response(response,formdata=df,callback=self.parse_login)
    def parse_login(self,response):
        if 'Welcome Liu' in response.text:
            yield from super().start_requests()


