# WebSpider0403
My object thumb
## The spider source code in Pycharm.
GetCityInfo.py  
UrlSeed.py  
GetWeatherData.py  
ToCsv.py  
RunThis.py  
SourceData.csv --同下--  
## Show data in Jupyter
1.ClearData.ipynb  
2.DataScreen.ipynb  
3.DataBy2019.ipynb  
4.AllYearsData.ipynb  
5.Line.ipynb  
6.WeatherCountPie.ipynb  
7.Pool.ipynb  
FinalData.csv  
SourceData.csv  --同上--  
## 结果在ResultData
数据分析时一共提出了几个问题:
1. 哈尔滨从2011年到2019年所有年份的温度走向是什么样的?
通过代码绘制出如图line1.png，影响气候的主要因素是纬度、大气流、海陆分布和地形。纬度位置是影响气候的基本因素。不同地区的不同纬度是不同地区气温不同的主要原因。哈尔滨处在地球的北温带，受到太阳照射的程度跟地球公转时候自身倾角有关，公转周期温度图像与正弦函数类似，也就是说地球倾角幅度越小，说明温度变化越不大，通过图观察温度的变化上下浮动但是浮动不大，也就说明地球在这几年的倾角同样是拥有一定程度的变化，对自然环境会有一定的影响，但是对人类日常生活影响不是很大。
2. 那么哈尔滨2019年最高温最低温分别在那几个月份?
从图DataBy2019.png以30天为一个月可以通过图形看出2019年哈尔滨最低温是在1月份，2019年哈尔滨最高温是在6月份。可以看出是非常符合温带气候的，十分的跌宕起伏，可以对比一下热带气候的新加坡图2019Singapore.png，新加坡典型的热带气候全年的温度起伏就比较平缓。
3. 哈尔滨历史温度是什么样的?
图AllYearsData.png同样也是跌宕起伏的图像，每年的全年季节温差都较大，也能看出历年的气温变化也并不是突然升高或降低气温，也还是有个过度的。
在数据筛选中发现哈尔滨历年来如图data2.png最高的温度竟然高达37℃。
查一下是哪年，如图所示,是在2014年的6月1日，那是否2014年全年的温度都偏高?如图line.png所展示，答案是否定的，2014年整体来说还是很普通的一年。
4. 哈尔滨历年的天气怎么样?
如图pi1.png所示9年来天气多云天数加起来要比晴天多，为了去除干扰项，只把排行在前五的天气数据列出来。如图pi2.png为去除杂项的图，直观的展示还是晴天比较多。
5. 最后温度的变化和风力有没有关系？
查看一下他们的相关系数图data3.png，可以用Pandas库提供的相关系数矩阵函数Corr（）.
由此看出风力和日期是没有关系的，并且风力也会影响到温度，只是影响不大。
6.  最后利用协方差看一下风力和最低温是否有关系？如图data4.png。
有关系，而且关系很大，说明如果风力越大，最低温越低，这和人体体感其实也差不多。
