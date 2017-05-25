# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    count = scrapy.Field()

class MovieItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    star = scrapy.Field()
    info = scrapy.Field()

class CommonItem(scrapy.Item):
    """DataBase-Oriented"""
    url = scrapy.Field()
    #详情页host
    source = scrapy.Field()
    id = scrapy.Field()
    #站点名
    site = scrapy.Field()
    # 站点名
    template_id = scrapy.Field()
    #全局唯一ID,source+id拼接
    uuid = scrapy.Field()
    exception_code = scrapy.Field()
    exception = scrapy.Field()
    other_parameter = scrapy.Field()
    domain = scrapy.Field()
    classify = scrapy.Field()
    subclass= scrapy.Field()


