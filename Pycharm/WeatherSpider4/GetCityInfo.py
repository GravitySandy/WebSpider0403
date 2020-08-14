# coding: utf-8

import requests
from lxml import etree


# 获取黑龙江省主要城市列表
# 返回城市英文名字列表
# 将总共的城市进行计数：并返回一共有多少城市

def get_city_infomation(url):  # print("开始获取主要城市列表")
    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    resp = requests.get(url, headers=DEFAULT_REQUEST_HEADERS)
    # 爬取传入的网页
    html = resp.content.decode('utf-8')  # 将爬取到的网页进行编码更改
    page = etree.HTML(html)  # 将爬取到的网页转换为etree类型

    cityurl = page.xpath('//dd//a/@href')  # 利用xpath解析网页 获取里面的类似与“ /lishi/haerbin.html ”的值

    citysList = []  # 创建一个城市列表的空数组，用于下面循环的存储
    for data in cityurl[:]:
        sub_data = data.split('/lishi/')[1].split('.')[0]  # 给爬取的“ /lishi/haerbin.html ”进行切片操作，取出要的“ haerbin ”部分
        citysList.append(sub_data[:])  # 并且  将“ haerbin ”类型的值添加进城市列表
    # print(citys)

    CityLen = len(citysList)  # 看看到底有多少城市
    # print("共有"+str(CityLen)+"个城市")

    citysTuple = tuple(citysList)  # 该操作将返回的城市列表改为元组，保证城市列表的顺序安全
    return citysTuple, CityLen  # 返回分别为城市列表与城市总数

if __name__ == '__main__':
    a = "http://www.tianqihoubao.com/lishi/heilongjiang.htm"
    print(len(get_city_infomation(a)[0][0:20]))
    print(get_city_infomation(a)[0])
    print("■" * 122)
    print(get_city_infomation(a)[0][0:20])
    print("■" * 122)
    print(get_city_infomation(a)[1])

