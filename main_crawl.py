from config import COLLECTIONS, LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME, USER_AGENTS, URL
from config import START_MONTH, START_YEAR, END_MONTH, END_YEAR
from cal_diy import CalStr
import config as conf
import requests
from lxml import etree
import random
import time
import pymongo
from pymongo.errors import DuplicateKeyError
import logging
import json
import re
import os
import threading
import sys
import io

sys.setrecursionlimit(100000)


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


class News(object):
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)

    def __init__(self, column):
        self.column = column  # 新闻栏目（股票频道、债券频道等）
        self.start_year = START_YEAR
        self.start_month = START_MONTH
        self.end_year = END_YEAR
        self.end_month = END_MONTH
        # self.url = None  # 该新闻对应的url
        # self.topic = None  # 新闻标题
        # self.date = None  # 新闻发布日期
        # self.content = None  # 新闻的正文内容
        # self.author = None  # 新闻作者
        # self.source = None  # 来源
        self.collection = self.client[DB_NAME][COLLECTIONS[self.column]]
        if self.column in ["股票频道", "债券频道", "基金频道", "财经新闻", "银行频道", "外汇新闻", "保险频道"]:
            self.url_column = URL[self.column]
        elif self.column in ["银行监管"]:
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
        if "页面没有找到" in response.text:
            return
        if year >= 2015:
            content = tree_node.xpath('//div[@class="texttit_m1"]//p//text()')
            if '.klinehk{margin:0 auto 20px;} ' in content:
                content = content[:content.index('.klinehk{margin:0 auto 20px;} ')]
            content = ''.join(content).replace("\u3000", ' ').replace("\r\n", '\n')
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
                         "source": source, "content": content, "year": year,
                         "crawl_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                         }
            try:
                logger.info(str(news_dict))
            except:
                pass
            try:
                self.collection.insert_one(news_dict)
            except DuplicateKeyError as e:
                pass

        else:
            content = tree_node.xpath(
                '//div[@class="textmain tmf14 jrj-clear"]//text() | //div[@id="IDNewsDtail"]//text()')
            if '.klinehk{margin:0 auto 20px;} ' in content:
                content = content[:content.index('.klinehk{margin:0 auto 20px;} ')]
            content = ''.join(content).replace("\u3000", ' ').replace("\r\n", '\n')
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
                         "source": source, "content": content, "year": year,
                         "crawl_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                         }
            try:
                logger.info(str(news_dict))
            except:
                pass
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
            # thr = threading.Thread(target=self.parse_page, args=(start_url, year_month[:4]))
            # thr.setDaemon(False)
            # thr.start()
            self.parse_page(start_url, year_month[:4])

    def parse_page(self, url, year=2020, first=True):
        # href:
        # //ul[@class="list"]/li/a/@href
        # next page
        # //p[@class="page_newslib"]/a/@href
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        response = requests.get(url, headers=headers)
        # print(response.text)
        response.encoding = response.apparent_encoding
        tree_node = etree.HTML(response.text)
        if self.column in ["股票频道", "债券频道", "基金频道", "财经新闻", "银行频道", "外汇新闻", "保险频道"]:
            news_list = tree_node.xpath('//ul[@class="list"]/li')
            for node in news_list:
                try:
                    href = node.xpath('./a/@href')[0]
                    creat_time = node.xpath('./span/text()')[0]
                    title = node.xpath('./a/text()')[0]
                    # thr = threading.Thread(target=self.getnews, args=(href, creat_time, title, year))
                    # thr.setDaemon(False)
                    # thr.start()
                    print(href)
                    self.getnews(href, creat_time, title, year)
                except:
                    pass

            # 判断next page
            if first:
                try:
                    total_page = int(tree_node.xpath('//p[@class="page_newslib"]/a[last()-1]/text()')[-1])
                    for i in range(2, total_page + 1):
                        url = url.split("_")[0] + "_" + str(i) + '.shtml'
                        print("*" * 30)
                        print(url)
                        self.parse_page(url, year, False)
                except:
                    pass

        elif self.column in ["银行监管"]:
            news_list = tree_node.xpath('//div[@class="newlist"]/ul/li')
            for node in news_list:
                try:
                    href = node.xpath('.//a/@href')[0]
                    creat_time = node.xpath('.//i/text()')[0]
                    year = creat_time.split("-")[0]
                    title = node.xpath('.//a/text()')[0]
                    # thr = threading.Thread(target=self.getnews, args=(href, creat_time, title, year))
                    # thr.setDaemon(False)
                    # thr.start()
                    print(href)
                    print(year)
                    self.getnews(href, creat_time, title, year)
                except:
                    pass

            # 判断next page
            if first:
                try:
                    total_page = int(tree_node.xpath('//p[@class="page_newslib"]/a[last()-2]/text()')[-1])
                    print(total_page)
                    for i in range(2, total_page + 1):
                        url = re.split(r'/jgdt', url)[0] + "/" + "jgdt-{}.shtml".format(str(i))
                        print("*" * 30)
                        print(url)
                        self.parse_page(url, year, False)
                except:
                    pass

    def regular_start(self):
        self.parse_page(self.url_column)


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    
    
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    log_path = os.getcwd() + '/Logs/'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_name = log_path + rq + 'news.log'
    logfile = log_name
    
    # 第二步，创建一个handler，用于写入日志文件
    st = logging.StreamHandler()
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    st.setLevel(logging.WARNING)  # 输出到file的log等级的开关
#     st.setLevel(logging.DEBUG)  # 输出到file的log等级的开关


    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    st.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(st)

    news = News("股票频道")
    news.crawl_start()

#     news = News("银行监管")
#     news.regular_start()
