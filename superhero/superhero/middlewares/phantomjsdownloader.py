# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui

class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        self.cap = webdriver.DesiredCapabilities.PHANTOMJS
        self.cap["phantomjs.page.settings.resourceTimeout"] = 1000
        self.cap["phantomjs.page.settings.loadImages"] = True
        self.cap["phantomjs.page.settings.disk-cache"] = True
        self.cap["phantomjs.page.customHeaders.Cookie"] = 'CNZZDATA2724999=3cnzz_eid%3D648782242-1493886478-%26ntime%3D1493886478;UM_distinctid=15bd2d2548362b-0c32ca55b11511-396a7807-13c680-15bd2d25485c78;buvid3=A6FE0A15-A8A2-4B57-BC33-CFE7536A211F19744infoc;fts=1493890652;pgv_pvi=4486182912;pgv_si=s5642047488;'

        self.driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs', desired_capabilities=self.cap)
        # wait = ui.WebDriverWait(self.driver, 10)
    def VisitPersonPage(self, url, spider):
        print('正在加载网站.....')
        self.driver.get(url)
        time.sleep(1)
        # 翻到底，详情加载
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execute_script(js)
        # time.sleep(5)
        content = self.driver.page_source.encode('utf-8', 'ignore')
        print('网页加载完毕.....')
        return content

    def __del__(self):
        self.driver.quit()