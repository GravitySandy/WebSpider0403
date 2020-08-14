import pandas as pd

def TransAddcsv(tdf):
	csv1 = pd.read_csv("WeatherData2.csv")
	df3 = tdf.to_csv(tdf+".csv",mode = 'a',header = False,index = False)
	print("Add Successful")