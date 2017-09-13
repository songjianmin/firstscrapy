#!usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class CourseItem(scrapy.Item):

    #课程标题
    title = scrapy.Field()

    #课程url
    url = scrapy.Field()

    #课程标题图片
    image_url = scrapy.Field()

    #课程描述
    introduction = scrapy.Field()

    #学习人数
    student = scrapy.Field()

if __name__ == '__main__':
    course = CourseItem()
    course['title'] = "语文"
    print (course['title'])
    print (course.get('title'))
    print (course.keys())   