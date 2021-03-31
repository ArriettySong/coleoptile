# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sun Mar 28 21:53:58 2021

@author: huyaxue
"""
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from urllib.request import Request, urlopen


def request_data(url):
    request = Request( url)
    html = urlopen(request)
    #获取数据
    data = html.read()
    # print(type(data))
    # print(data.decode("gbk"))
    # 转换成字符串
    # res = data.decode("gbk")
    res = data.decode("utf-8")

    return res

sina_url = "http://hq.sinajs.cn/list=f_"
gtimg_url = "http://qt.gtimg.cn/q=sz"
url = sina_url
fundid = "162411"
# print(request_data(url+fundid))
# print(request_data("http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,100000&dt=1595929218181&atfc=&onlySale=0"))pmr
# 历史净值
print(request_data("http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=110022&page=1&sdate=2019-01-01&edate=2019-02-13&per=20"))

# https://blog.csdn.net/otter1010/article/details/105884256

# 场外基金使用的接口时sina接口。格式如下（在浏览器中输入，能够收到结果）：
# http://hq.sinajs.cn/list=f_100032
# 可以一次申请查询多个基金代码，比如
# http://hq.sinajs.cn/list=f_100032,f_162411
# 返回的结果样式为：
# var hq_str_f_100032="富国中证红利指数增强A,1.087,2.934,1.091,2021-03-17,35.8668";
# var hq_str_f_162411="华宝标普油气上游股票(QDII-LOF)A,0.42,0.42,0.4327,2021-03-16,123.95";

# 场内股票/基金使用的接口。格式如下（在浏览器中输入，能够收到结果）：
# http://qt.gtimg.cn/q=sz162411
# 可以一次申请查询多个股票/ETF代码，比如
# http://qt.gtimg.cn/q=sz162411,sh512900
# 返回的结果样式为：
# v_sz162411="51~华宝油气~162411~0.418~0.420~0.418~646966~132009~514957~0.417~98674~0.416~424165~0.415~200691~0.414~107991~0.413~60844~0.418~87463~0.419~47880~0.420~63673~0.421~35770~0.422~52912~~20210318103803~-0.002~-0.48~0.419~0.416~0.418/646966/26990879~646966~2699~~~~0.419~0.416~0.71~~~0.00~0.462~0.378~0.98~604667~0.417~~~~~~2699.0879~0.0000~0~ ~LOF~44.14~~~~"; v_sh512900="1~证券基金~512900~1.035~1.029~1.028~82567~32026~50542~1.034~4600~1.033~2716~1.032~375~1.031~400~1.030~328~1.035~500~1.036~2401~1.037~3015~1.038~2508~1.039~368~~20210318103802~0.006~0.58~1.040~1.028~1.035/82567/8541728~82567~854~~~~1.040~1.028~1.17~~~0.00~1.132~0.926~1.37~-373~1.035~~~~~~854.1728~0.0000~0~ ~ETF~-14.46~~~~";

# 新浪股票api：http://hq.sinajs.cn/list=sz002307,sh600928
