# -*- coding: utf-8 -*-
import scrapy
from ..items import ToscrapeBookItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//article[@class="product_pod"]/div[@class="image_container"]/a')
        for sel in le.extract_links(response):
            yield scrapy.Request(sel.url,callback=self.parse_book)

        le = LinkExtractor(restrict_xpaths='//div[2]//li[@class="next"]')
        links = le.extract_links(response)
        if links:
            yield scrapy.Request(links[0].url,callback=self.parse)



    def parse_book(self,response):
        book=ToscrapeBookItem()
        book['name']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').extract_first()
        book['price']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').extract_first()
        book['review_rating']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').re_first('star-rating ([a-zA-Z]+)')
        book['review_num']=response.xpath('//tr[7]/td/text()').extract_first()
        book['upc']=response.xpath('//tr[1]/td/text()').extract_first()
        book['stock']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()').re_first('\((\d+) available\)')
        yield book
        pass
