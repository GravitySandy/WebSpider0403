# coding: utf-8

import pandas

def save_as_csv(data):
	sourceList = pandas.DataFrame(data, index=['Citys', 'ymd', 'Weather', 'highTemp', 'lowTemp', 'wind'])
	listToDataframe = sourceList.stack()
	endDataframe = listToDataframe.unstack(0)
	try:
		endDataframe.to_csv('SourceData.csv', mode='x', index=False, encoding='utf-8')
	except FileExistsError:
		endDataframe.to_csv('SourceData.csv', mode='a', index=False, encoding='utf-8', header=False)
	# print(endDataframe)
	return endDataframe
