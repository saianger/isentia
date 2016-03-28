import scrapy
from scrapy.selector import Selector
from isentia.items import IsentiaItem

# create spider class
class IsentiaSpider(scrapy.Spider):
    # define the name of the spider
    name = "isentia"
    # url and domain definition
    allowed_domains = ["theguardian.com"]
    start_urls = [
        "http://www.theguardian.com/au",
    ]
    
    # mothod to extract exact url for certain article
    def parse(self, response):
        for href in response.xpath('//h2[@class="fc-item__title"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    # method to extract relevant information about a particular article
    def parse_dir_contents(self, response):
        for sel in response.xpath('//html'):
            item = IsentiaItem()
            item['headline'] = ''.join(sel.xpath('//title/text()').extract())
            item['author'] = ''.join(sel.xpath('//meta[@name="author"]/@content').extract())
            item['link'] = ''.join(sel.xpath('//link[@rel="canonical"]/@href').extract())
            item['article'] = ''.join(sel.xpath('//div[@class="content__article-body from-content-api js-article__body"]/p/text()').extract())
            yield item