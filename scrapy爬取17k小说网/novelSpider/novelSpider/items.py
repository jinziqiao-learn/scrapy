# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 1.小说名称
    name = scrapy.Field()
    # 2.作者名称
    writer = scrapy.Field()
    # 3.小说类型
    type = scrapy.Field()
    # 4.更新章节
    newest = scrapy.Field()
    # 5.更新时间
    updateTime=scrapy.Field()
    # 6.字数
    number = scrapy.Field()
    # 7.更新状态
    update = scrapy.Field()
    # #8.内容简介
    novel_breif=scrapy.Field()
    #9.月点击量
    monthclickCount=scrapy.Field()
