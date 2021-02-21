import scrapy


class TxmsSpider(scrapy.Spider):
    name = 'txms'
    allowed_domains = ['v.qq.com']
    start_urls = ['http://v.qq.com/']

    def parse(self, response):
        pass
