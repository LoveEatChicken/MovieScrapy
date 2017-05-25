#!/usr/bin/env python
# coding: utf-8

__author__ = 'Ycz'

from bs4 import BeautifulSoup
from des_base_spider import BaseSpider
from superhero.items import CommonItem
from scrapy import FormRequest
import hashlib
import re
import json

cookies = {
            '_T_WM': 'cba59eeeaecfff96a08f5b0ba2aaebbc',
            'gsid_CTandWM':	'4uqeadc51EBAEACFXzfVzo5Xd4K',
            'SUB': '_2A251Q63MDeRxGeNJ71AW9i3OwjiIHXVWzzOErDV6PUJbkdANLU6lkW1fSRLJD5j4ch8eTJ6hNlUqg0JuBg..',
            'M_WEIBOCN_PARAMS':	'luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home'
        }
headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
class WeiBoHotSpider(BaseSpider):

    name = 'weibohot'
    allowed_domains = ["weibo.com"]

    def __init__(self, **kw):
        super(WeiBoHotSpider, self).__init__(**kw)

    def start_requests(self):
        url = 'http://weibo.com/'
        yield FormRequest(url,
                            headers=headers,
                            cookies=cookies,
                            callback=self.parse)

    def parse(self, response):
        data = response.body
        print 'dddd ------ %s' % data
        # data = data.encode('utf-8')
        soup = BeautifulSoup(data, "html5lib")
        ul_tags = soup.find_all('ul', class_='ul_text')
        # print 'ul tag -------- %s' % ul_tags
        for ul_tag in ul_tags:
            li_tags = ul_tag.find_all('li', class_='li_text clearfix', recursive=False)
            for li_tag in li_tags:
                item = CommonItem()
                item['source'] = self.source
                item['site'] = self.site
                item['classify'] = self.classify
                item['domain'] = self.domain
                item['subclass'] = self.subclass
                item['template_id'] = self.template_id
                weibo_a_tag = li_tag.find('a', recursive=False)
                item['url'] = weibo_a_tag['href']
                # print 'url ------- %s' % item['url']
                # m = re.match(r'(http://weibo.com/p/)([\s\S]*)(\?[\s\S]*)', item['url'])
                # # print 'iddddd ------- %s' % m.group(2)
                # item['id'] = m.group(2)
                m2 = hashlib.md5()
                m2.update(item['url'])
                print 'm22 --------- %s' % m2.hexdigest()
                item['id'] = m2.hexdigest()
                weibo_dic = {}
                weibo_dic['title'] = weibo_a_tag['title']
                origin_read_count = li_tag.find('span', recursive=False).text
                #print 'readcount ------- %s unit ---- %s' % (origin_read_count, origin_read_count[-1])
                read_count_unit = origin_read_count[-1]
                no_unit_float = float(origin_read_count[:-1].encode('utf-8'))
                if read_count_unit == u'万':
                    no_unit_float *= 10000
                elif read_count_unit == u'亿':
                    no_unit_float *= 100000000
                else:
                    pass
                # format(no_unit_float, '.4e')
                # print 'eeeeee ---- %s' % format(no_unit_float, '.4e')
                weibo_dic['read_count'] = no_unit_float
                item['other_parameter'] = weibo_dic
                print item
                yield item







