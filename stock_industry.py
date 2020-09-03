from config import INCREASE, DROP, TURNOVER_AMOUNT_A, TURNOVER_AMOUNT_D, TURNOVER_MONEY_A, TURNOVER_MONEY_D, \
    TURNOVER_RATE_A, TURNOVER_RATE_D, ZJLX, STOCK_KEYWORD  # 个股
from config import INDUSTRY, HS_INDEX_URL, YQ_URL  # 行业、大盘、要闻
from config import COLLECTIONS, LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME, USER_AGENTS, URL
import requests
from lxml import etree
import random
import time
import pymongo
from pymongo.errors import DuplicateKeyError
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options


class StockIndustry(object):
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)

    def __init__(self, column):
        self.column = column
        self.collection = self.client[DB_NAME][COLLECTIONS[self.column]]

    def individual_stocks(self, keyword):
        item = STOCK_KEYWORD[keyword]
        for title, url in item.items():
            self.page_parse_stock(title, url, keyword)

    def page_parse_stock(self, title, url, keyword):
        print(title)
        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)
        chrome_options = Options()
        chrome_options.add_argument('--user-agent={}'.format(headers))  # 设置请求头的User-Agent
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
        # chrome_options.add_argument('headless')  # 浏览器不提供可视化页面
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        tree_node = etree.HTML(driver.page_source)
        # 表头
        # heads = tree_node.xpath()
        # 表内容
        keyword_to_idx = {"涨幅": 4,
                          "跌幅": 4,
                          "换手率高": 9,
                          "换手率低": 9,
                          "成交量高": 6,
                          "成交量低": 6,
                          "成交金额高": 7,
                          "成交金额低": 7,
                          "资金流动": 5}
        content_list = []
        if keyword != "资金流动":
            contents = tree_node.xpath('//div[@id="con12_1"]/div[2]//tr')
            for stock in contents:
                code = stock.xpath('./td[@t="code"]//text()')[0]
                stock_name = stock.xpath('./td[@t="name"]//text()')[0]
                item = stock.xpath('./td[{}]//text()'.format(keyword_to_idx[keyword]))[0]
                # print(code)
                # print(stock_name)
                # print(item)
                print([code, stock_name, item])
                content_list.append([code, stock_name, item])
        elif keyword == "资金流动":
            contents = tree_node.xpath('//div[@class="bd"]/div[4]//tr')
            for stock in contents:
                code = stock.xpath('./td[@t="code"]//text()')[0]
                stock_name = stock.xpath('./td[@t="name"]//text()')[0]
                item = stock.xpath('./td[{}]//text()'.format(keyword_to_idx[keyword]))[0]
                # print(code)
                # print(stock_name)
                # print(item)
                print([code, stock_name, item])
                content_list.append([code, stock_name, item])
        stock_rank = {"_id": url, "title": title, "url": url, "keyword": keyword, "rank": content_list,
                      "crawl_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                      }
        print(stock_rank)
        driver.close()
        try:
            self.collection.insert_one(stock_rank)
        except DuplicateKeyError as e:
            pass


if __name__ == '__main__':
    '''
    个股：
    STOCK_KEYWORD = {"涨幅": INCREASE,
                 "跌幅": DROP,
                 "换手率高": TURNOVER_RATE_D,
                 "换手率低": TURNOVER_RATE_A,
                 "成交量高": TURNOVER_AMOUNT_D,
                 "成交量低": TURNOVER_AMOUNT_A,
                 "成交金额高": TURNOVER_MONEY_D,
                 "成交金额低": TURNOVER_MONEY_A,
                 "资金流动": ZJLX}
    '''
    stk = StockIndustry("个股排行")
    stk.individual_stocks("换手率高")  # "涨幅","跌幅","换手率高","换手率低","成交量高","成交量低","成交金额高","成交金额低","资金流动"
