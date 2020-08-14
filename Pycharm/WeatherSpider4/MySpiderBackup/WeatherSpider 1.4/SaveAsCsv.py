# coding: utf-8

import pandas as pd

def save_as_csv(data):
	df = pd.DataFrame(data, index=['Citys','ymd', 'Weather', 'highTemp','lowTemp','wind'])
	df2 = df.stack()
	df3 = df2.unstack(0)
	print('*'*64)
	#转存到csv
	df3.to_csv('data.csv',index = False,encoding = 'utf-8')
	print(df3)
	return df3
