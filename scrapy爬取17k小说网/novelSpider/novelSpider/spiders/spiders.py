# -*- coding: utf-8 -*-
# from imp import reload
import scrapy
from novelSpider.items import NovelspiderItem
import scrapy.http.request

class NovelSpider(scrapy.Spider):
    name = 'novelSpider2'  # 爬虫的名字
    allowed_domains = ['17k.com']
    # 定义需要爬取的页面
    start_urls = []
    for i in range(1, 2):#添加所有需要获取信息的地址
        # url1 = 'https://www.17k.com/all/book/1_0_0_0_0_0_0_0_' + str(i) + '.html' # 文史政治
        url2 = 'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_' + str(i) + '.html'#男生类别
        # url3 = 'https://www.17k.com/all/book/3_0_0_0_0_0_0_0_' + str(i) + '.html'#女生类别
        # url4 = 'https://www.17k.com/all/book/4_0_0_0_0_0_0_0_' + str(i) + '.html'#个性化
        # start_urls.append(url1)
        start_urls.append(url2)
        # start_urls.append(url3)
        # start_urls.append(url4)
    #     url11='https://www.17k.com/all/book/2_21_0_0_0_0_0_0_' + str(i) + '.html'#玄幻奇幻 334
    #     url12 = 'https://www.17k.com/all/book/2_24_0_0_0_0_0_0_' + str(i) + '.html'#仙侠武侠 334
    #     url13 = 'https://www.17k.com/all/book/2_3_0_0_0_0_0_0_' + str(i) + '.html'#都市小说 334
    #     # url14 = 'https://www.17k.com/all/book/2_22_0_0_0_0_0_0_' + str(i) + '.html'#历史军事 305
    #     url15 = 'https://www.17k.com/all/book/2_23_0_0_0_0_0_0_' + str(i) + '.html'#游戏竞技 334
    #     url16 = 'https://www.17k.com/all/book/2_14_0_0_0_0_0_0_' + str(i) + '.html'#科幻末世 334
    #     url21 = 'https://www.17k.com/all/book/3_17_0_0_0_0_0_0_' + str(i) + '.html'#都市言情 334
    #     url22 = 'https://www.17k.com/all/book/3_5_0_0_0_0_0_0_' + str(i) + '.html'#古装言情 334
    #     url23 = 'https://www.17k.com/all/book/3_18_0_0_0_0_0_0_' + str(i) + '.html'#幻想言情 334
    #     # url24 = 'https://www.17k.com/all/book/3_20_0_0_0_0_0_0_' + str(i) + '.html'#浪漫青春 58
    #     url31 = 'https://www.17k.com/all/book/4_7_0_0_0_0_0_0_' + str(i) + '.html'#悬疑小说 334
    #     url32 = 'https://www.17k.com/all/book/4_16_0_0_0_0_0_0_' + str(i) + '.html'#二次元 334
    #     # url33 = 'https://www.17k.com/all/book/4_27_0_0_0_0_0_0_' + str(i) + '.html'  # 爆笑小说 78
    #     url34 = 'https://www.17k.com/all/book/4_25_0_0_0_0_0_0_' + str(i) + '.html'  # 自述小说 334
    #     url35 = 'https://www.17k.com/all/book/4_28_0_0_0_0_0_0_' + str(i) + '.html'  # 青春小说 334
    #     # url36 = 'https://www.17k.com/all/book/4_26_0_0_0_0_0_0_' + str(i) + '.html'  # 情感小说 309
    #     start_urls.append(url11)
    #     start_urls.append(url12)
    #     start_urls.append(url13)
    #     start_urls.append(url15)
    #     start_urls.append(url16)
    #     start_urls.append(url21)
    #     start_urls.append(url22)
    #     start_urls.append(url23)
    #     start_urls.append(url31)
    #     start_urls.append(url32)
    #     start_urls.append(url34)
    #     start_urls.append(url35)
    # for i in range(1, 306):
    #     url14 = 'https://www.17k.com/all/book/2_22_0_0_0_0_0_0_' + str(i) + '.html'  # 历史军事 305
    #     start_urls.append(url14)
    # for i in range(1, 59):
    #     url24 = 'https://www.17k.com/all/book/3_20_0_0_0_0_0_0_' + str(i) + '.html'  # 浪漫青春 58
    #     start_urls.append(url24)
    # for i in range(1, 79):
    #     url33 = 'https://www.17k.com/all/book/4_27_0_0_0_0_0_0_' + str(i) + '.html'  # 爆笑小说 78
    #     start_urls.append(url33)
    # for i in range(1, 310):
    #     url36 = 'https://www.17k.com/all/book/4_26_0_0_0_0_0_0_' + str(i) + '.html'  # 情感小说 309
    #     start_urls.append(url36)

    def parse(self, response):#获取每一页的小说详情页地址
        content_list = response.xpath("//table/tbody/tr[@class]")
        if content_list == []:
            return
        for content in content_list:
            url = content.xpath("td[@class='td3']/span/a/@href").extract_first('')#获取的href为//www.17k.com/book/2967395.html格式
            details_url = 'https:' + url#详情页的地址
            yield scrapy.Request(details_url, dont_filter=False, callback=self.get_details)#将地址传入get_details方法

    def get_details(self,response):#获取详情页中小说的信息
        item = NovelspiderItem()
        name = response.xpath("//h1/a/text()").extract_first('书名缺失').strip().replace(",", "/")
        writer = response.xpath("//div[@class='author']/a[@class='name']/text()").extract_first('作者缺失').strip()
        type = response.xpath("//div[@class='infoPath']/div/a[3]/text()").extract_first('类型缺失').strip()#
        newest = response.xpath("//dl[@class='NewsChapter']/dd/ul/li/a/text()").extract_first('更新缺失').strip()
        updateTime=response.xpath("//dl[@class='NewsChapter']/dd/ul/li/span/text()").extract_first('更新时间缺失').strip()
        number = response.xpath("//div[@class='BookData']/p[2]/em/text()").extract_first('字数缺失').strip()
        update = response.xpath("//div[@class='label']/a[1]/span/text()").extract_first('无更新状态').strip()
        novel_breif = response.xpath("//p[@class='intro']/a/text()").extract_first('简介缺失').strip()
        monthclickCount=response.xpath("//*[@id='monthclickCount']/text()").extract_first('无月点击量').strip()
        item['name'] = name
        item['writer'] = writer
        item['type'] = type
        item['newest'] = newest
        item['updateTime'] = updateTime
        item['number'] = number
        item['update'] = update
        item['novel_breif'] = novel_breif
        item['monthclickCount'] = monthclickCount
        yield item