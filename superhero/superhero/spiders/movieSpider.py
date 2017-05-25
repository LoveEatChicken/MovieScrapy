#!/usr/bin/env python
# coding: utf-8

__author__ = 'Ycz'

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from superhero.utils.parse_util import Parse_Util
from superhero.items import MovieItem

page_base_uri = "http://www.yingshidaquan.cc/vod-show-id-1-p-%d.html"
detail_base_uri = "http://www.yingshidaquan.cc%s"

class BilibiliSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["yingshidaquan.cc"]
    def start_requests(self):
        MAX_PAGE_COUNT = 2
        for page in range(1, MAX_PAGE_COUNT):
            url = page_base_uri % int(page)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        list_tag = soup.find('ul', class_='mlist').find_all('li', recursive=False)
        for li_tag in list_tag:
            item = MovieItem()
            a_tag = li_tag.find('a', recursive=False)
            detail_link = detail_base_uri % a_tag['href']
            item['img'] = a_tag.find('img')['src']
            item['star'] = a_tag.find('i').text
            info_tag = li_tag.find('div', class_='info')
            item['name'] = info_tag.find('h2').find('a')['title']

            info_detail = info_tag.find_all('p', recursive=False)
            info_dic = Parse_Util.structure_parameter_dic(info_detail, u'：')
            print info_dic
            item['info'] = info_dic
            yield Request(detail_link, callback=self.parse_movie_detail, meta={'item': item})

    def parse_movie_detail(self, response):
        item = response.meta['item']
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        down_url_tags = soup.find_all('div', class_='addss')
        link = []
        for div_tag in down_url_tags:
            link.append(div_tag.find('input')['value'])
        item['link'] = link
        yield item


