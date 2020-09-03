<div align="left">
    <img src='https://ftp.bmp.ovh/imgs/2020/08/b77a8439ea51e080.jpg' height="50" width="50" >
 </div>


![jrj_crawl](https://badgen.net/badge/JRJ/crawl?icon=github)
![GitHub license](https://badgen.net/github/license/HUANGZHIHAO1994/JRJ_crawl?color=green)

# JRJ_crawl

下面样本中的1，2按需修改config.py后运行main_crawl.py即可

样本中的3查看config.py中STOCK_KEYWORD后运行stock_industry.py

## 一.样本：

1."股票频道", "债券频道", "基金频道", "财经新闻", "银行频道", "外汇新闻", "保险频道"样本：

```python
{'_id': 'http://stock.jrj.com.cn/2019/05/04215627521858.shtml', 'title': '国金证券：美股的估值优势目前不复存在', 'url': 'http://stock.jrj.com.cn/2019/05/04215627521858.shtml', 'keyword': '', 'create_time': '2019-05-04 21:56:00', 'source': '证券时报网', 'content': '  证券时报e公司讯，国金证券(行情600109,诊股)认为，客观上讲，随着美股不断的创出历史新高，美股的估值优势目前不复存在，当前美股的估值处于历史估值中位数以上（尽管还没触及到历史的估值高点），后续美股的上涨更多的依赖于上市公司持续优异的业绩驱动，而这由美国自身经济和核心竞争力所决定。数据显示，截至于4月底，标普500指数、纳斯达克指数估值分别为19.1倍、34.5倍，高于2010年以来历史均值水平。', 'year': 2019, 'crawl_time': '2020-09-03 16:06:44'}
```

2."银行监管","保险监管"样本：

```python
{'_id': 'http://stock.jrj.com.cn/2019/05/04192127521561.shtml', 'title': '财政部长出席亚洲开发银行理事会第52届年会', 'url': 'http://stock.jrj.com.cn/2019/05/04192127521561.shtml', 'keyword': '', 'create_time': '2019-05-04 19:21:00', 'source': '证券时报网', 'content': '  证券时报e公司讯，5月3-4日，亚洲开发银行理事会第52届年会在斐济楠迪举行，财政部长刘昆率中国代表团出席会议。刘昆指出，在全球经济放缓、下行风险突出的背景下，亚太各国要结合本国国情，采取适当的宏观经济政策，保持经济稳定增长；要坚持多边主义，实现区域经济互利共赢；要有效防控金融风险，维护亚太经济金融稳定。中国政府不断创新和完善宏观调控、实施更大规模减税降费、防范和化解系统性金融风险，推动高质量发展。', 'year': 2019, 'crawl_time': '2020-09-03 08:13:02'}
```



3.“个股排行”样本

```python
`{'_id': 'http://summary.jrj.com.cn/gpph/sha_pl_d.shtml', 'title': 'URL_INCREASE_H', 'url': 'http://summary.jrj.com.cn/gpph/sha_pl_d.shtml', 'keyword': '涨幅', 'rank': [['688378', 'N奥来德', '51.25%'], ['605006', 'N山玻', '44.01%'], ['688277', '天智航', '19.99%'], ['688017', '绿的谐波', '16.35%'], ['688339', '亿华通', '15.36%'], ['688418', '震有科技', '14.79%'], ['600227', '圣济堂', '10.03%'], ['603919', '金徽酒', '10.01%'], ['605333', '沪光股份', '10.01%'], ['603156', '养元饮品', '10.01%'], ['605123', '派克新材', '10.00%'], ['603536', '惠发食品', '10.00%'], ['603877', '太平鸟', '10.00%'], ['600753', '东方银星', '9.99%'], ['600983', '惠而浦', '9.99%'], ['603959', '百利科技', '9.99%'], ['600993', '马应龙', '9.98%'], ['601798', '蓝科高新', '9.97%'], ['600397', '安源煤业', '9.96%'], ['688521', '芯原股份', '9.30%']], 'crawl_time': '2020-09-03 23:32:32'}
```

