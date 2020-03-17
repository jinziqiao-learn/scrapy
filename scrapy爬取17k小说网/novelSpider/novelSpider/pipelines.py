# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class NovelspiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        filename = 'novel_test.csv'
        # file1 = open(filename, 'w+', encoding='utf-8')
        file1 = open(filename, 'a+', encoding='utf-8')#以读写追加模式打开文件，不覆盖原数据
        self.writer = csv.writer(file1)
        self.writer.writerow(['小说名称', '作者名称', '小说类型', '更新章节', '更新时间', '字数', '更新状态','内容简介','月点击量'])#csv文档的头部

    def process_item(self, item, spider):
        name = item['name']
        writer = item['writer']
        type = item['type']
        newest = item['newest']
        updateTime = item['updateTime'].replace('更新时间：', '')#去掉多余的数据 <span class="time">更新时间：2019-06-28 12:30:48</span>
        number = item['number']
        update = item['update']
        novel_breif = item['novel_breif']
        monthclickCount = item['monthclickCount']
        #规整数据，去掉数据中的空格
        if name:
            item['name'] = name.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n', '|换行|').replace('\r',
                                                                                                                   '|换行|')
        if writer:
            item['writer'] = writer.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n', '|换行|').replace(
                '\r', '|换行|')
        if type:
            item['type'] = type.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n', '|换行|').replace('\r',
                                                                                                                   '|换行|')
        if newest:
            item['newest'] = newest.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n',
                                                                                               '|换行|').replace('\r',
                                                                                                               '|换行|')
        if updateTime:
            item['updateTime'] = updateTime.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n',
                                                                                                       '|换行|').replace(
                '\r', '|换行|')
        if number:
            item['number'] = number.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n', '|换行|').replace(
                '\r', '|换行|')
        if update:
            item['update'] = update.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n', '|换行|').replace(
                '\r', '|换行|')
        if novel_breif:
            item['novel_breif'] = novel_breif.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n',
                                                                                                         '|换行|').replace(
                '\r', '|换行|')
        if monthclickCount:
            item['monthclickCount'] = monthclickCount.strip().replace('\n', '|空格|').replace(' ', '|空格|').replace('\r\n',
                                                                                               '|换行|').replace('\r',
                                                                                                               '|换行|')

        novel = []
        novel.append([name, writer, type, newest, updateTime, number, update,novel_breif,monthclickCount])
        for n in novel:
            self.writer.writerow(n)#存入文件
        print('====' * 20)
        print('小说名字:', item['name'])
        print('小说作者:', item['writer'])
        print('小说类型:', item['type'])
        print('更新章节:', item['newest'])
        print('更新时间:',item['updateTime'])
        print('总字数:', item['number'])
        print('更新状态:', item['update'])
        print('内容简介:', item['novel_breif'])
        print('月点击量:', item['monthclickCount'])
        print('====' * 20)

def close_spider(self, spider):
    self.writer.close()#关闭打开的文件
