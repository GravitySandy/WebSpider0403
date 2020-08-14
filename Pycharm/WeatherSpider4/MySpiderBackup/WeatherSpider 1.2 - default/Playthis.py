# coding: utf-8

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

from sanwei import get_data
from chengshi import tianqiurl as turl
from heilongjiang import *
from run import transFormFun

url = 'http://www.tianqihoubao.com/weather/province.aspx?id=230000'

# print(turl(diming(url)))

print('*'*64)
transFormFun(get_data(turl(diming1(url))))
# transFormFun(get_data(turl(diming2(url))))
# transFormFun(get_data(turl(diming3(url))))
# transFormFun(get_data(turl(diming4(url))))
# transFormFun(get_data(turl(diming5(url))))
# transFormFun(get_data(turl(diming6(url))))
# transFormFun(get_data(turl(diming7(url))))
# transFormFun(get_data(turl(diming8(url))))
# transFormFun(get_data(turl(diming9(url))))
# transFormFun(get_data(turl(diming10(url))))
# transFormFun(get_data(turl(diming11(url))))
# transFormFun(get_data(turl(diming12(url))))
# transFormFun(get_data(turl(diming13(url))))


print('*'*64)
print('成功')