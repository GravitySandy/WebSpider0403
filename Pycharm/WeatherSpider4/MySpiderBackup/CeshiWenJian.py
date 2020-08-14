import requests
from bs4 import BeautifulSoup as bs
from GetWeatherData import get_data
from WeatherUrl import weather_Url as wurl
from GetCityInfo import get_city_infomation as gci

from SaveAsCsv import save_as_csv as tcsv

url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'

list1 = ["http://www.tianqihoubao.com/lishi/acheng/month/201812.html","http://www.tianqihoubao.com/lishi/anda/month/201812.html"]
list2 = wurl(gci(url))

listLen = len(list2)

def get_data2(url):	
	resp = requests.get(url)
	html = resp.content.decode('GBK')#print(resp.text)
	soup = bs(html,'lxml')

	title_list = soup.find_all('title')
	for data in title_list[:]:
		title0 = data.text.split("_")


	tr_list = soup.find_all('tr')
	cityName,dates,weathers,highTemps,lowTemps = [],[],[],[],[]
	for data in tr_list[1:]:
		sub_data = data.text.split()
		# print(sub_data)
		
	for data in tr_list[1:]:
		cityName.append(title0[2:-1])
		sub_data = data.text.split()
		dates.append(sub_data[0])
		weathers.append(''.join(sub_data[1:3]))
		highTemps.append(''.join(sub_data[3:4]))
		lowTemps.append(''.join(sub_data[5:6])) 
		

	print(cityName)
	print(dates,weathers,highTemps,lowTemps)
	return
		


for i in range(0,listLen):
	get_data2(list2[i])


