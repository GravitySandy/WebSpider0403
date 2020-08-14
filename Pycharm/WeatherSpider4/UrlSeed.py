# coding: utf-8

#从2011年1月到2018年12月的天气后报url ,并生成一个“地方”列表

def weather_Url(place) :
    htmlhref = []
    k = 0
    for city in place:
        for year in range(2011,2020):              #起始年份--结束年份
            for month in range(1,13):              #月份
                if month < 10:
                    mm = str(year)+'0'+str(month)  #在1-9月份前面加上0
                else:
                    mm = str(year)+str(month)
                htmlhref.append('http://www.tianqihoubao.com/lishi/' + city + '/month/'+ mm +'.html')
    htmlhrefTuple = tuple(htmlhref)
    return htmlhrefTuple

if __name__  == '__main__':
    a = ['acheng', 'haerbin']
    print(weather_Url(a))
