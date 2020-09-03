#  随机请求头设置
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'
]

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'JRJ_News'
COLLECTIONS = {"股票频道": "Stock",
               "债券频道": "Bond",
               "基金频道": "Fund",
               "财经新闻": "Finance",
               "外汇新闻": "Forex",
               "银行频道": "Bank",
               "保险频道": "Insurance",
               "银行监管": "BankReg",
               "保险监管": "InsurReg",
               "个股排行": "StockRank",
               "大盘速览": "MarketView"}

# url_demo 设置

URL = {"股票频道": "stock",
       "债券频道": "bond",
       "基金频道": "fund",
       "财经新闻": "finance",
       "银行频道": "bank",
       "外汇新闻": "forex",
       "保险频道": "Insurance",
       "银行监管": "http://bank.jrj.com.cn/list/jgdt.shtml",
       "保险监管": "http://insurance.jrj.com.cn/list/jgdt.shtml ",
       }

# 起始时间、起始月份、结束时间、结束月份
# "股票频道", "债券频道", "基金频道", "财经新闻", "银行频道", "外汇新闻", "保险频道"爬取时根据需要调整
START_YEAR = 2019
START_MONTH = 5
END_YEAR = 2020
END_MONTH = 12
