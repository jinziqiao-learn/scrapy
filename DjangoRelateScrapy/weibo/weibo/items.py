# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from microblog.models import HotSpot


class WeiboItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = HotSpot
