# coding: utf-8

import requests
from lxml import etree


# 传入一个“地方”网址，获取“地方”的天气信息：日期、天气、最高温度、最低温度、风级风向


def get_data(url):
    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    resp = requests.get(url, headers=DEFAULT_REQUEST_HEADERS)
    # 爬取传入的网页
    html = resp.content.decode('gbk')  # 将爬取到的网页进行编码更改
    htmlChange = etree.HTML(html)  # 将爬取到的网页转换为etree类型
    # print(html)

    cityName = htmlChange.xpath('//div/h1/text()')  # 利用xpath找到城市名称列表
    citys = []  # 定义一个空的城市名称列表
    for data in cityName[:]:
        sub_data = data.split()[0]  # 获得类型为“阿城历史天气预报”的值
        citys.append(sub_data[:-6])  # 将“阿城历史天气预报”的值中“历史天气预报”舍弃
    # citys


    date = htmlChange.xpath('//tr/td[1]/a/text()')  # 利用xpath找到日期的位置
    daTes = []  # 定义一个空的日期列表
    for data in date[:]:
        sub_data = data.split()[0]  # 提取出日期的数据
        daTes.append(sub_data[:])  # 将日期数据添加到日期列表
    # daTes


    weather = htmlChange.xpath('//tr/td[2]/text()')  # 利用xpath找到天气数据的位置
    weaThers = []  # 定义一个空的天气数据列表
    for data in weather[1:]:
        sub_data = data.split()[0] + '/' + data.split()[1].split('/')[1]
        # 提取数据
        weaThers.append(sub_data[:])  # 生成列表
    # weaThers


    temp = htmlChange.xpath('//tr/td[3]/text()')  # 利用xpath找到温度的位置
    highTemp, lowTemp = [], []  # 定义两个空的列表分辨代表高温列表和低温列表
    for data in temp[1:]:
        highTemp_data = data.split()[0]  # 提取高温数据
        lowTemp_data = data.split()[2]  # 提取低温数据
        highTemp.append(highTemp_data)  # 写入高温列表
        lowTemp.append(lowTemp_data)  # 写入高温列表
    # print(highTemp)
    # print(lowTemp)


    wind = htmlChange.xpath('//tr/td[4]/text()')  # 利用xpath找到风向风力的位置
    windData = []  # 定义一个空的风向风力列表
    for data in wind[1:]:
        sub_data = data.split()[0] + data.split()[1] + '/' + data.split()[2].split('/')[1] + data.split()[3]
        # 利用切片方法与字符拼接提取出需要的数据（链式操作）
        windData.append(sub_data[:])  # 写入数据
    # windData


    return citys,daTes,weaThers,highTemp,lowTemp,windData  # 返回5种参数


if __name__ == '__main__':
    a = ['http://www.tianqihoubao.com/lishi/haerbin/month/201812.html',
         'http://www.tianqihoubao.com/lishi/hulan/month/201812.html',
         'http://www.tianqihoubao.com/lishi/acheng/month/201812.html']
    # print(get_data(a))
    count = 0
    q = len(a)
    for i in a:
        count += 1
        # save_as_csv(get_data(a))
        print(get_data(i)[1][0].split('年')[0], end='年')
        print(get_data(i)[0][0], end='==》')
        print("loading : " + str(int(count * 100 / q)) + " %")
        if count == q:
            print('Finish')