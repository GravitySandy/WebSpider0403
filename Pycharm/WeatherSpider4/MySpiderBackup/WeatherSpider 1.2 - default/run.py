# coding: utf-8

# import requests
import pandas as pd
# import numpy as np
# from bs4 import BeautifulSoup as bs
import csv

# from sanwei import get_data
# from chengshi import tianqiurl as turl
# from heilongjiang import *

def transFormFun(data):
	df = pd.DataFrame(data, index=['ymd', 'Tianqi', 'high','low'])
	df2 = df.stack()
	df3 = df2.unstack(0)
	print('*'*64)
	#转存到csv
	df3.to_csv("WeatherData2.csv",index = False,encoding = 'utf-8')
	print(df3)
	return df3
