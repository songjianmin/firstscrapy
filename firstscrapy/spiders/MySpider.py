#!usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from firstscrapy.CourseItems import CourseItem

class MySpider(scrapy.Spider):

    #用于区别Spider
    name = "MySpider"

    #允许访问的域
    allowed_domains = ["imooc.com"]

    #爬取得地址
    start_urls = ["http://www.imooc.com/course/list"]

    def parse(self,response):

        #实例一个容器保存爬取的信息
        eachcourse = CourseItem()

        #这部分时爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #先获取每个课程的div
        # print (response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'))
        for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
            #获取每个div中的课程路径
            eachcourse['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            #获取div中的课程标题
            eachcourse['title'] = box.xpath('.//h3/text()').extract()[0]
            #获取div中的标题图片地址
            eachcourse['image_url'] = box.xpath('.//@src').extract()[0]
            #获取div中的学生人数
            eachcourse['student'] = box.xpath('.//span[2]/text()').extract()[0]
            #获取div中的课程简介
            eachcourse['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            #获取页码
            eachcourse['page'] = response.xpath('//a[@class="active text-page-tag"]/text()').extract()[0]
            #返回信息
            yield eachcourse

            #url跟进开始
            #获取下一页的url信息
            url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
            if url:
                #讲信息组合成下一页的url
                page = 'http://www.imooc.com' + url[0]
                #返回url
                yield scrapy.Request(page,callback=self.parse)
            #url跟进结束









