# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import DownloadItem
class DownloaderSpider(scrapy.Spider):
    name = 'downloader'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le=LinkExtractor(restrict_xpaths="//li[@class='toctree-l2']")
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_example)
        pass
    def parse_example(self,response):
        herf=response.xpath('/html/body/div[4]/div[1]/div/div/div/p[1]/a/@href').extract_first()
        url=response.urljoin(herf)
        example=DownloadItem()
        example['file_urls']=[url]
        return example


        pass


