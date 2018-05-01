#-*- coding:utf-8-*-

import scrapy
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor
class BooksSpider(scrapy.Spider):

    name = "books"

    start_urls=['http://books.toscrape.com/']

    def start_requests(self):
        yield scrapy.Request('http://books.toscrape.com/',
                             callback=self.parse,
                             headers={'User-Agent':'Mozilla/5.0'},
                             dont_filter=True)


    def parse(self, response):
        for sel in response.css('article.product_pod'):
            book=BookItem()
            book['name']=sel.xpath('./h3/a/@title').extract_first()
            book['price']=sel.xpath('./div[2]/p[1]/text()').extract_first()
            # article / div[2] / p[1]
            yield book
        #next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
        #next_url=response.xpath('//div[2]//li[@class="next"]/a/@href').extract_first()

        le=LinkExtractor(restrict_xpaths='//div[2]//li[@class="next"]')
        links=le.extract_links(response)


        if links:
            next_url=links[0].url
            yield scrapy.Request(next_url,callback=self.parse)



        pass

    pass









