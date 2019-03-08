#商管程式設計二第三周上課內容 #datetime
import datetime
d1 = datetime.datetime(2005,5,3)
print(d1)
d2 = datetime.datetime(2019,2,20,8,5,20)
print(d2)
print(d2.date()) #只抓日期
print(d2.time()) #只抓時間
print(d2.date().weekday()) #抓星期幾  0~6 0 monday 6  sunday
print(datetime.date.today()) #抓今天日期
# get value of each slot
print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)
#difference of datetime
d3 = datetime.datetime(1998,2,5,8,5,20)
d4 = datetime.datetime(1999,2,1,22,4,15)
diff = d4-d3
print(diff) #datetime.timedalta(361,50335) 
print(diff.days)
print(diff.seconds)
#time shifting by timedalta
diff2  = datetime.timedelta(days = 3,seconds = 4) 
d5 = d3+diff2 #加上3天4秒
print(d5)
#datetime 轉成 str
print(str(d5))
#輸出 1998-02-08 08:05:24
print(d5.strftime('%Y-%m-%d')) #只要年月日
#輸出 1998-02-08
print(d5.strftime('%b %d , %Y')) #只要年月日
#輸出 Feb 08 , 1998
print(d5.strftime('%Y-%m-%d %H:%M:%S')) #只要年月日時分秒
# 輸出 1998-02-08 08:05:24
print(d4.strftime('%Y-%m-%d %I:%M:%S %p , %A')) #只要年月日時分秒 %I 分上下午 am pm
# 輸出 1998-02-08 08:05:24 AM , Sunday

#str 轉成 datetime
dstr = '2007-03-04 21:08:12'
date_convert = datetime.datetime.strptime(dstr,'%Y-%m-%d %H:%M:%S')
print(type(date_convert))  #datetime.datetime(2007,3,4,21,8,12)