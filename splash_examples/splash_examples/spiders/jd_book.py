# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy import Request

lua_script='''
function main(splash)
    splash:go(splash.args.url)
    splash:wait(2)
    splash:runjs("document.getElementsByClassName('page')[0].scrollIntoView(ture)")
    splash:wait(2)
    return splash:html()
end
'''

class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']
    base_url='https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python'

    def start_requests(self):
        yield Request(self.base_url,callback=self.parse_urls,dont_filter=True)
    def parse_urls(self,response):
        total=int(response.xpath('//*[@id="J_resCount"]/text()').re('([0-9]+)')[0])
        pageNum=total//60 + (1 if total % 60 else 0)
        for i in range(pageNum):
            url='{}&page={}'.format(self.base_url,2*i+1)
            yield SplashRequest(url,endpoint='execute',args={'lua_source':lua_script},cache_args=['lua_source'])
    def parse(self, response):
        for sel in response.css('ul.gl-warp.clearfix>li.gl-item'):
            yield {
                'name':sel.css('div.p-name').xpath('string(.//em)').extract_first(),
                'price':sel.css('div.p-price i::text').extract_first(),
            }

        pass
