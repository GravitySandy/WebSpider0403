# coding: utf-8


import requests
from bs4 import BeautifulSoup as bs


from WeatherUrl import weather_Url as wurl
from GetCityInfo import get_city_infomation as gci

#获得输入城市的url之后返回:城市、日期、天气、最高温度、最低温度。

def get_data(url):
	# print(url)
	cityName,dates,weathers,htemps,ltemps = [],[],[],[],[]
	for link in url:
		print(link[34:-18]+'的'+link[-11:-5]+"月份")		
		resp = requests.get(link)
		html = resp.content.decode('GBK')
		soup = bs(html,'lxml')

		tr_list = soup.find_all('tr')
		title_list = soup.find_all('title')

		for data in title_list[:]:
			title0 = data.text.split("_")
		
		for data in tr_list[1:]:
			cityName.append(title0[2:-1])
			sub_data = data.text.split()
			dates.append(sub_data[0])
			weathers.append(''.join(sub_data[1:3]))
			htemps.append(''.join(sub_data[3:4]))
			ltemps.append(''.join(sub_data[5:6]))
	return (cityName,dates,weathers,htemps,ltemps) 
