#!/usr/bin/env python
# coding: utf-8
import scrapy
from bs4 import BeautifulSoup
from superhero.items import BilibiliItem

class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    allowed_domains = ["bilibili.com"]
    start_urls = ["http://www.bilibili.com/video/ent-Kichiku-1.html"]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        # container_tag = soup.find('div', class_='container-row area-22')
        # section_r_tag = container_tag.find('div', class_='b-r')
        # list_tag = section_r_tag.find('ul', class_='rlist')
        # for li_tag in list_tag:
        #     item = BilibiliItem()
        #     item['count'] = li_tag['data-gk']
        #     item['date'] = li_tag['data-tg']
        #     item['title'] = li_tag.find('div', class_='title t').text
        #     item['link'] = li_tag.find('a', class_='rl-info')['href']
        #     yield item


