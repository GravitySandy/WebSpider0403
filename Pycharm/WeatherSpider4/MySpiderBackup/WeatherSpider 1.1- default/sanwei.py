# coding: utf-8


import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

from chengshi import tianqiurl as turl
from heilongjiang import diming 

#获得输入城市的url之后返回三个数值，日期、天气、温度。

def get_data(url):
	# print(url)
	dates,weathers,htemps,ltemps = [],[],[],[]
	for link in url:
		print(link[34:-18]+'的'+link[-11:-5])		
		resp = requests.get(link)
		html = resp.content.decode('GBK')
		soup = bs(html,'html.parser')
		tr_list = soup.find_all('tr')

		for data in tr_list[1:]:
			sub_data = data.text.split()
			dates.append(sub_data[0])
			weathers.append(''.join(sub_data[1:3]))
			htemps.append(''.join(sub_data[3:4]))
			ltemps.append(''.join(sub_data[5:6]))
	return (dates,weathers,htemps,ltemps) 

# url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'
# st1ep = diming(url)
# st2ep = turl(st1ep)
# get_data(st2ep)