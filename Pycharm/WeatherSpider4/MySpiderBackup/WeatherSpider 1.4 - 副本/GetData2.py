import requests
from lxml import etree

def Void2(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')#print(resp.text)
	page = etree.HTML(html)
	# print(html)

	date = page.xpath('//tr/td[1]/a/text()')
	weather = page.xpath('//tr/td[2]/text()')
	temp = page.xpath('//tr/td[3]/text()')

	daTes,weaThers,highTemps,lowTemps = [],[],[],[]

	# print(date)
	for data in date[:]:
			sub_data = data.split()
			daTes.append(sub_data[0])
			# print(daTes)
	# print(daTes)
			
	# print(weather)
	for data in weather[1:]:
			sub_data = data.split()
			weaThers.append(sub_data[0:3])
			# print(weaThers)
	# print(weaThers)


	# print(temp)
	for data in temp[1:]:
			sub_data = data.split()
			# print(sub_data)
			highTemps.append(sub_data[0])
			lowTemps.append(sub_data[2])

			# print(highTemps)
			# print(lowTemps)
	# print(highTemps)
	# print(lowTemps)
	print(daTes,weaThers,highTemps,lowTemps)
	return daTes,weaThers,highTemps,lowTemps

a = "http://www.tianqihoubao.com/lishi/acheng/month/201812.html"
Void2(a)