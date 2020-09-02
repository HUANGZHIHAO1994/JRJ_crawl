from config import COLLECTIONS, LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME, USER_AGENTS, URL
from cal_diy import CalStr
import config as conf
import requests
from lxml import etree
import random
import time
import pymongo
import codecs
from urllib import request, parse
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from pymongo.errors import DuplicateKeyError
import logging
import json
import re
import os


class News(object):
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)

    def __init__(self, column, start_year, start_month, end_year, end_month):
        self.column = column  # 新闻栏目（股票频道、债券频道等）
        self.start_year = start_year
        self.start_month = start_month
        self.end_year = end_year
        self.end_month = end_month
        # self.url = None  # 该新闻对应的url
        # self.topic = None  # 新闻标题
        # self.date = None  # 新闻发布日期
        # self.content = None  # 新闻的正文内容
        # self.author = None  # 新闻作者
        # self.source = None  # 来源
        self.collection = self.client[DB_NAME][COLLECTIONS[self.column]]
        if self.column in ["股票频道", "债券频道", "基金频道"]:
            self.url_column = URL[self.column]

    # 如果url符合解析要求，则对该页面进行信息提取
    def getnews(self, url, creat_time, title, year):
        # 获取页面所有元素
        # 15年之后和之前xpath写法不同,15年之前无keyword
        keyword, source, content = [], '', ''
        year = eval(year)
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        tree_node = etree.HTML(response.text)
        if year >= 2015:
            content = tree_node.xpath('//div[@class="texttit_m1"]//text()')
            if '.klinehk{margin:0 auto 20px;} ' in content:
                content = content[:content.index('.klinehk{margin:0 auto 20px;} ')]
            content = ''.join(content)
            source = tree_node.xpath('//span[contains(text(),"来源")]//text()')
            while '来源：' in source:
                source.remove('来源：')
            while '' in source:
                source.remove('')
            while '\r\n' in source:
                source.remove('\r\n')
            source = ''.join(source)
            keyword = ''
            # logger.info(content)
            # logger.info(source)
            # logger.info(str(keyword))

            news_dict = {"_id": url, "title": title, "url": url, "keyword": keyword, "create_time": creat_time,
                         "source": source, "content": content,
                         "crawl_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                         }
            logger.info(str(news_dict))
            try:
                self.collection.insert_one(news_dict)
            except DuplicateKeyError as e:
                pass

        else:
            content = tree_node.xpath(
                '//div[@class="textmain tmf14 jrj-clear"]//text() | //div[@id="IDNewsDtail"]//text()')
            if '.klinehk{margin:0 auto 20px;} ' in content:
                content = content[:content.index('.klinehk{margin:0 auto 20px;} ')]
            content = ''.join(content)
            source = tree_node.xpath('//span[contains(text(),"来源")]//text()')
            while '来源：' in source:
                source.remove('来源：')
            while '' in source:
                source.remove('')
            while '\r\n' in source:
                source.remove('\r\n')
            source = ''.join(source)

            # logger.info(content)
            # logger.info(source)
            # logger.info(str(keyword))

            news_dict = {"_id": url, "title": title, "url": url, "keyword": keyword, "create_time": creat_time,
                         "source": source, "content": content,
                         "crawl_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                         }
            logger.info(str(news_dict))
            try:
                self.collection.insert_one(news_dict)
            except DuplicateKeyError as e:
                pass

    def crawl_start(self):
        c = CalStr(self.start_year, self.start_month, self.end_year, self.end_month)
        date_list = c.calendarlist()
        # print(date_list)
        # 可写成yield迭代器
        for year_month, day in date_list:
            start_url = 'http://{}.jrj.com.cn/xwk/{}/{}_1.shtml'.format(self.url_column, year_month, day)
            self.parse_page(start_url, year_month[:4])

    def parse_page(self, url, year, first=True):
        print(url)
        # href:
        # //ul[@class="list"]/li/a/@href
        # next page
        # //p[@class="page_newslib"]/a/@href
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        tree_node = etree.HTML(response.text)
        news_list = tree_node.xpath('//ul[@class="list"]/li')
        for node in news_list:
            try:
                href = node.xpath('./a/@href')[0]
                creat_time = node.xpath('./span/text()')[0]
                title = node.xpath('./a/text()')[0]
                print(href)
                print(creat_time)
                print(title)
                self.getnews(href, creat_time, title, year)
            except:
                pass

        # 判断next page
        if first:
            try:
                total_page = int(tree_node.xpath('//p[@class="page_newslib"]/a[last()-1]/text()')[-1])
                print(total_page)
                for i in range(2, total_page + 1):
                    url = url.split("_")[0] + "_" + str(i) + '.shtml'
                    print(url)
                    self.parse_page(url, False)
            except:
                pass


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    log_path = os.getcwd() + '/Logs/'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_name = log_path + rq + 'penal.log'
    logfile = log_name
    st = logging.StreamHandler()
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    st.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    st.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(st)

    news = News("股票频道", 2007, 5, 2020, 8)
    news.crawl_start()
