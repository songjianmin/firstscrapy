#!usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class MySpider(scrapy.Spider):

    #用于区别Spider
    name = "MyFirstSpider"

    #允许访问的域
    allowed_domains = []

    #爬取得地址
    start_urls = []

    def pars(self,response):
        pass



