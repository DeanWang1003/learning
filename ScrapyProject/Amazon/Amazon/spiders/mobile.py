import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=mobile+phone&crid=1IRH5Y4YGQ6N1&sprefix=mobile%2Caps%2C399&ref=nb_sb_ss_ts-doa-p_1_6']

    def parse(self, response):
        print(response.xpath('//div[@class="s-main-slot s-result-list s-search-results sg-row"]/div//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract())
