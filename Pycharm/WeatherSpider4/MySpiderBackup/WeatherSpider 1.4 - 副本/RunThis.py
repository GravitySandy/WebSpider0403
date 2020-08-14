# coding: utf-8

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

from GetWeatherData import get_data
from WeatherUrl import weather_Url as wurl
# from GetCityInfo import *
from GetCityInfo import get_city_infomation as gci
from SaveAsCsv import save_as_csv as tcsv

url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'

print('*'*64)
#print(wurl(gci(url)))
dataList = get_data(wurl(gci(url)))
tcsv(dataList)

print('*'*64)
print('成功')