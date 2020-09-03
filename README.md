<div align="left">
    <img src='https://ftp.bmp.ovh/imgs/2020/08/b77a8439ea51e080.jpg' height="50" width="50" >
 </div>
![jrj_crawl](https://badgen.net/badge/JRJ/crawl?icon=github)
![GitHub license](https://badgen.net/github/license/HUANGZHIHAO1994/traffic_crawl?color=green)

# JRJ_crawl

按需修改config.py后运行main_crawl.py即可

## 一.样本：

1."股票频道", "债券频道", "基金频道", "财经新闻", "银行频道", "外汇新闻", "保险频道"样本：

```python
{'_id': 'http://stock.jrj.com.cn/2019/05/04215627521858.shtml', 'title': '国金证券：美股的估值优势目前不复存在', 'url': 'http://stock.jrj.com.cn/2019/05/04215627521858.shtml', 'keyword': '', 'create_time': '2019-05-04 21:56:00', 'source': '证券时报网', 'content': '  证券时报e公司讯，国金证券(行情600109,诊股)认为，客观上讲，随着美股不断的创出历史新高，美股的估值优势目前不复存在，当前美股的估值处于历史估值中位数以上（尽管还没触及到历史的估值高点），后续美股的上涨更多的依赖于上市公司持续优异的业绩驱动，而这由美国自身经济和核心竞争力所决定。数据显示，截至于4月底，标普500指数、纳斯达克指数估值分别为19.1倍、34.5倍，高于2010年以来历史均值水平。', 'year': 2019, 'crawl_time': '2020-09-03 16:06:44'}
```

2."银行监管","保险监管"样本：

```python
{'_id': 'http://stock.jrj.com.cn/2019/05/04192127521561.shtml', 'title': '财政部长出席亚洲开发银行理事会第52届年会', 'url': 'http://stock.jrj.com.cn/2019/05/04192127521561.shtml', 'keyword': '', 'create_time': '2019-05-04 19:21:00', 'source': '证券时报网', 'content': '  证券时报e公司讯，5月3-4日，亚洲开发银行理事会第52届年会在斐济楠迪举行，财政部长刘昆率中国代表团出席会议。刘昆指出，在全球经济放缓、下行风险突出的背景下，亚太各国要结合本国国情，采取适当的宏观经济政策，保持经济稳定增长；要坚持多边主义，实现区域经济互利共赢；要有效防控金融风险，维护亚太经济金融稳定。中国政府不断创新和完善宏观调控、实施更大规模减税降费、防范和化解系统性金融风险，推动高质量发展。', 'year': 2019, 'crawl_time': '2020-09-03 08:13:02'}
```




