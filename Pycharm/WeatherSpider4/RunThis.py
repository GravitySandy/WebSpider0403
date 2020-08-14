# coding: utf-8

import requests
import pandas

from GetCityInfo import get_city_infomation
from UrlSeed import weather_Url
from GetWeatherData import get_data
from ToCsv import save_as_csv


url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'
url2 = "http://www.tianqihoubao.com/lishi/heilongjiang.htm"


print('*'*64)
cityName = get_city_infomation(url2)[0][0:1]
cityNameNum = len(cityName)
print("cityName:" + str(cityName))
print("cityName:"+str(cityNameNum))


weatherUrl =  weather_Url(cityName)
print('weatherUrl'+ str(weatherUrl))
print(type(weatherUrl))
print('weatherUrl'+str(len(weatherUrl)))

print('*'*64)

# for k in get_data(list(weatherUrl)):
#     print(type(k))
# print(len(k))





count = 0
q = len(weatherUrl)
for a in weatherUrl:
    count += 1
    save_as_csv(get_data(a))
    # print(get_data(a)[1][0].split('月')[0], end='月')
    # print(get_data(a)[0][0], end='==》')
    print("loading : " + str("%.2f"%(count * 100 / q)) + " %")
    if count == q:
        print('Finish')

print('*'*64)