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
               "板块排行": "IndustryRank",
               "大盘速览": "MarketView",
               "实时要闻": "RealTimeNews"}

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

# 个股排行
# 涨跌幅等
INCREASE = {
    "URL_INCREASE_HS": "http://summary.jrj.com.cn/gpph/sa_pl_d.shtml",  # 沪深两市(d 代表降序排）
    "URL_INCREASE_H": "http://summary.jrj.com.cn/gpph/sha_pl_d.shtml",  # 沪市
    "URL_INCREASE_S": "http://summary.jrj.com.cn/gpph/sza_pl_d.shtml",  # 深市
    "URL_INCREASE_H_B": "http://summary.jrj.com.cn/gpph/shb_pl_d.shtml",  # 沪市B股
    "URL_INCREASE_S_B": "http://summary.jrj.com.cn/gpph/szb_pl_d.shtml",  # 深市B股
    "URL_INCREASE_ZXB": "http://summary.jrj.com.cn/gpph/zxb_pl_d.shtml",  # 中小板
    "URL_INCREASE_CYB": "http://summary.jrj.com.cn/gpph/cyb_pl_d.shtml"}  # 创业板

DROP = {
    "URL_DROP_HS": "http://summary.jrj.com.cn/gpph/sa_pl_a.shtml",  # 沪深两市
    "URL_DROP_H": "http://summary.jrj.com.cn/gpph/sha_pl_a.shtml",  # 沪市
    "URL_DROP_S": "http://summary.jrj.com.cn/gpph/sza_pl_a.shtml",  # 深市
    "URL_DROP_H_B": "http://summary.jrj.com.cn/gpph/shb_pl_a.shtml",  # 沪市B股
    "URL_DROP_S_B": "http://summary.jrj.com.cn/gpph/szb_pl_a.shtml",  # 深市B股
    "URL_DROP_ZXB": "http://summary.jrj.com.cn/gpph/zxb_pl_a.shtml",  # 中小板
    "URL_DROP_CYB": "http://summary.jrj.com.cn/gpph/cyb_pl_a.shtml"}  # 创业板

# 换手率 D是降序也就是换手率从高到低
TURNOVER_RATE_D = {
    "URL_TURNOVER_RATE_D_HS": "http://summary.jrj.com.cn/gpph/sa_tr_d.shtml",  # 沪深两市
    "URL_TURNOVER_RATE_D_H": "http://summary.jrj.com.cn/gpph/sha_tr_d.shtml",  # 沪市
    "URL_TURNOVER_RATE_D_S": "http://summary.jrj.com.cn/gpph/sza_tr_d.shtml",  # 深市
    "URL_TURNOVER_RATE_D_H_B": "http://summary.jrj.com.cn/gpph/shb_tr_d.shtml",  # 沪市B股
    "URL_TURNOVER_RATE_D_S_B": "http://summary.jrj.com.cn/gpph/szb_tr_d.shtml",  # 深市B股
    "URL_TURNOVER_RATE_D_ZXB": "http://summary.jrj.com.cn/gpph/zxb_tr_d.shtml",  # 中小板
    "URL_TURNOVER_RATE_D_CYB": "http://summary.jrj.com.cn/gpph/cyb_tr_d.shtml"}  # 创业板

TURNOVER_RATE_A = {
    "URL_TURNOVER_RATE_A_HS": "http://summary.jrj.com.cn/gpph/sa_tr_a.shtml",  # 沪深两市
    "URL_TURNOVER_RATE_A_H": "http://summary.jrj.com.cn/gpph/sha_tr_a.shtml",  # 沪市
    "URL_TURNOVER_RATE_A_S": "http://summary.jrj.com.cn/gpph/sza_tr_a.shtml",  # 深市
    "URL_TURNOVER_RATE_A_H_B": "http://summary.jrj.com.cn/gpph/shb_tr_a.shtml",  # 沪市B股
    "URL_TURNOVER_RATE_A_S_B": "http://summary.jrj.com.cn/gpph/szb_tr_a.shtml",  # 深市B股
    "URL_TURNOVER_RATE_A_ZXB": "http://summary.jrj.com.cn/gpph/zxb_tr_a.shtml",  # 中小板
    "URL_TURNOVER_RATE_A_CYB": "http://summary.jrj.com.cn/gpph/cyb_tr_a.shtml"}  # 创业板

# 成交额
TURNOVER_MONEY_D = {
    "URL_TURNOVER_MONEY_D_HS": "http://summary.jrj.com.cn/gpph/sa_tm_d.shtml",  # 沪深两市
    "URL_TURNOVER_MONEY_D_H": "http://summary.jrj.com.cn/gpph/sha_tm_d.shtml",  # 沪市
    "URL_TURNOVER_MONEY_D_S": "http://summary.jrj.com.cn/gpph/sza_tm_d.shtml",  # 深市
    "URL_TURNOVER_MONEY_D_H_B": "http://summary.jrj.com.cn/gpph/shb_tm_d.shtml",  # 沪市B股
    "URL_TURNOVER_MONEY_D_S_B": "http://summary.jrj.com.cn/gpph/szb_tm_d.shtml",  # 深市B股
    "URL_TURNOVER_MONEY_D_ZXB": "http://summary.jrj.com.cn/gpph/zxb_tm_d.shtml",  # 中小板
    "URL_TURNOVER_MONEY_D_CYB": "http://summary.jrj.com.cn/gpph/cyb_tm_d.shtml"}  # 创业板

TURNOVER_MONEY_A = {
    "URL_TURNOVER_MONEY_A_HS": "http://summary.jrj.com.cn/gpph/sa_tm_a.shtml",  # 沪深两市
    "URL_TURNOVER_MONEY_A_H": "http://summary.jrj.com.cn/gpph/sha_tm_a.shtml",  # 沪市
    "URL_TURNOVER_MONEY_A_S": "http://summary.jrj.com.cn/gpph/sza_tm_a.shtml",  # 深市
    "URL_TURNOVER_MONEY_A_H_B": "http://summary.jrj.com.cn/gpph/shb_tm_a.shtml",  # 沪市B股
    "URL_TURNOVER_MONEY_A_S_B": "http://summary.jrj.com.cn/gpph/szb_tm_a.shtml",  # 深市B股
    "URL_TURNOVER_MONEY_A_ZXB": "http://summary.jrj.com.cn/gpph/zxb_tm_a.shtml",  # 中小板
    "URL_TURNOVER_MONEY_A_CYB": "http://summary.jrj.com.cn/gpph/cyb_tm_a.shtml"}  # 创业板

# 成交量
TURNOVER_AMOUNT_D = {
    "URL_TURNOVER_AMOUNT_D_HS": "http://summary.jrj.com.cn/gpph/sa_ta_d.shtml",  # 沪深两市
    "URL_TURNOVER_AMOUNT_D_H": "http://summary.jrj.com.cn/gpph/sha_ta_d.shtml",  # 沪市
    "URL_TURNOVER_AMOUNT_D_S": "http://summary.jrj.com.cn/gpph/sza_ta_d.shtml",  # 深市
    "URL_TURNOVER_AMOUNT_D_H_B": "http://summary.jrj.com.cn/gpph/shb_ta_d.shtml",  # 沪市B股
    "URL_TURNOVER_AMOUNT_D_S_B": "http://summary.jrj.com.cn/gpph/szb_ta_d.shtml",  # 深市B股
    "URL_TURNOVER_AMOUNT_D_ZXB": "http://summary.jrj.com.cn/gpph/zxb_ta_d.shtml",  # 中小板
    "URL_TURNOVER_AMOUNT_D_CYB": "http://summary.jrj.com.cn/gpph/cyb_ta_d.shtml"}  # 创业板

TURNOVER_AMOUNT_A = {
    "URL_TURNOVER_AMOUNT_A_HS": "http://summary.jrj.com.cn/gpph/sa_ta_a.shtml",  # 沪深两市
    "URL_TURNOVER_AMOUNT_A_H": "http://summary.jrj.com.cn/gpph/sha_ta_a.shtml",  # 沪市
    "URL_TURNOVER_AMOUNT_A_S": "http://summary.jrj.com.cn/gpph/sza_ta_a.shtml",  # 深市
    "URL_TURNOVER_AMOUNT_A_H_B": "http://summary.jrj.com.cn/gpph/shb_ta_a.shtml",  # 沪市B股
    "URL_TURNOVER_AMOUNT_A_S_B": "http://summary.jrj.com.cn/gpph/szb_ta_a.shtml",  # 深市B股
    "URL_TURNOVER_AMOUNT_A_ZXB": "http://summary.jrj.com.cn/gpph/zxb_ta_a.shtml",  # 中小板
    "URL_TURNOVER_AMOUNT_A_CYB": "http://summary.jrj.com.cn/gpph/cyb_ta_a.shtml"}  # 创业板

# 个股资金流向排行
# http://summary.jrj.com.cn/zjlx/gglr.shtml
# 5日 http://summary.jrj.com.cn/zjlx/gglr.shtml?day=5day
ZJLX = {"1_DAY": "http://summary.jrj.com.cn/zjlx/gglr.shtml",
        "5_DAY": "http://summary.jrj.com.cn/zjlx/gglr.shtml?day=5day",
        "10_DAY": "http://summary.jrj.com.cn/zjlx/gglr.shtml?day=10day",
        "20_DAY": "http://summary.jrj.com.cn/zjlx/gglr.shtml?day=20day"}

STOCK_KEYWORD = {"涨幅": INCREASE,
                 "跌幅": DROP,
                 "换手率高": TURNOVER_RATE_D,
                 "换手率低": TURNOVER_RATE_A,
                 "成交量高": TURNOVER_AMOUNT_D,
                 "成交量低": TURNOVER_AMOUNT_A,
                 "成交金额高": TURNOVER_MONEY_D,
                 "成交金额低": TURNOVER_MONEY_A,
                 "资金流动": ZJLX}

# 行业板块排行
# 证监会行业 http://summary.jrj.com.cn/zjhhy/index.shtml
# 地域板块 http://summary.jrj.com.cn/dybk/index.shtml
# 行业板块 http://summary.jrj.com.cn/hybk/index.shtml
# 全球行业 http://summary.jrj.com.cn/qqhy/index.shtml
# 概念板块 http://summary.jrj.com.cn/gnbk/index.shtml
INDUSTRY = {
    "ZJHHY": "http://summary.jrj.com.cn/zjhhy/index.shtml",
    "HYBK": "http://summary.jrj.com.cn/hybk/index.shtml",
    "DYBK": "http://summary.jrj.com.cn/dybk/index.shtml",
    "QQHY": "http://summary.jrj.com.cn/qqhy/index.shtml",
    "GGBK": "http://summary.jrj.com.cn/gnbk/index.shtml"
}

# 大盘
HS_INDEX_URL = "http://summary.jrj.com.cn/hszs/index.shtml"

# 7 * 24 行业要闻
YQ_URL = "http://finance.jrj.com.cn/yaowen/"
