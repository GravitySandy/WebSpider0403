# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs

#获取黑龙江省主要城市列表

def diming1(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[13:-117]:#a[13:-34]正确数据    a[13:-117]测试采样
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[13:-117]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys
# print(diming('http://www.tianqihoubao.com/weather/province.aspx?id=230000'))


def diming2(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[19:-100]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[19:-100]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


def diming3(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[25:-94]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[25:-94]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


def diming4(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[31:-88]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[31:-88]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


def diming5(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[37:-82]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[37:-82]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


def diming6(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[43:-76]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[43:-76]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


def diming7(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[49:-70]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[55:-64]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming8(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[55:-64]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[55:-64]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming9(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[61:-58]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[61:-58]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming10(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[67:-52]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[67:-52]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming11(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[73:-46]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[73:-46]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming12(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[79:-40]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[79:-40]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys

def diming13(url):
	resp = requests.get(url)
	html = resp.content.decode('GBK')
	soup = bs(html,'html.parser')
	tr_list = soup.find_all('tr')
	for data in tr_list[1:]:
		sub_data = data.text.split()
	a = soup.find_all('a')
	for href in a[85:-34]:
		ahref = href.get('href')
	t1 = soup.find_all('a')
	citys = []
	for t2 in t1[85:-34]:
		t3 = t2.get('href').split('/')
		t4 = t3[1].split('.')
		citys.append(t4[0])
	return citys


















