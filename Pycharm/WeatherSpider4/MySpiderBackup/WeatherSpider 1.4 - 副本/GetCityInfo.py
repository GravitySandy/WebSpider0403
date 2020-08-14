# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs

#获取黑龙江省主要城市列表

def get_city_infomation(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'lxml')

	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	citySection = soup.find_all('a')

	for href in citySection[13:-34]:#a[13:-34]正确数据    a[13:-115]测试采样
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[13:-34]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys
# print(diming('http://www.tianqihoubao.com/weather/province.aspx?id=230000'))
