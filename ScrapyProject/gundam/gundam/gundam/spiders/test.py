import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.78dm.net']
    start_urls = ['http://acg.78dm.net/ct/336252.html#dmrw']

    def parse(self, response):
        print(response.xpath(
            '//div[@class="show-list"]//li/a/text()').extract())

