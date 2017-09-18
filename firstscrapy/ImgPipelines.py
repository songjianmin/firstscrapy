#!usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    #通过抓取的图片url获取一个request用于下载
    def get_media_requests(self,item,info):
        #返回Request根据图片url'下载
        yield scrapy.Request(item['image_url'])

    #当下载请求完成后执行该方法
    def item_completed(self,results,item,info):
        #获取下载地址
        image_path = [ x['path'] for ok, x in results if ok]

        #判断是否成功
        if not image_path:
            raise DropItem("Item contains no images")
        #讲地址存入item
        print (image_path)
        item['image_path'] = image_path
        return item