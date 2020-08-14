# coding: utf-8

#从2011年1月到2018年12月的天气后报url    ,返回一个列表

def weather_Url(place) :   
    htmlhref = []
    k = 0
    for city in place:
        for year in range(2011,2019):#起始年份--结束年份
            for month in range(1,13):#月份
                if month < 10:
                    mm = str(year)+'0'+str(month)
                else:
                    mm = str(year)+str(month)
                htmlhref.append('http://www.tianqihoubao.com/lishi/' + city + '/month/'+mm+'.html') 
    return htmlhref
