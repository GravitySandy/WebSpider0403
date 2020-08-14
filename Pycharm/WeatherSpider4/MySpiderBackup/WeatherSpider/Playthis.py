# coding: utf-8

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

from sanwei import get_data
from chengshi import tianqiurl as turl
from heilongjiang import diming 

url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'

print('*'*64)
print(turl(diming(url)))

print('*'*64)
data = get_data(turl(diming(url)))

# print(data)
df = pd.DataFrame(data, index=['日期', '天气', '温度'])
df2 = df.stack()
df3 = df2.unstack(0)
print('*'*64)
df3.to_csv('WeatherData.csv',index = False,encoding = 'utf-8')
print(df3)