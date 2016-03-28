# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IsentiaItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()
    article = scrapy.Field()
    author = scrapy.Field()
