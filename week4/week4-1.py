#商管程式設計二第四周上課內容 #股票分析
#step1 : preprocess: remove chinese headline,convert to csv file ,remove all space
#step2 : sort data by stock and then by date
#step3 : prepare market return data
#step4 : for each stock: 
# 1. merge stock return with matket data by date
# 2. run regression
# 3. record the result
import csv
stock_data = []
with open('stock.txt','r',encoding='cp950') as f:
	for line in f:
		if '證券代碼	簡稱	年月日	報酬率％	市值(百萬元)	收盤價(元)' in line:
			continue
		code,abb,date,rr,mv,cp = line.strip().split('\t')
		stock_data.append([code,abb,date,rr,mv,cp])
with open ('stock_convet.csv','w',encoding='cp950') as f:
	f.write('COID,Name,MDATE,ROI,MV,CLOSE\n')
	for d in stock_data:
		f.write(d[0]+','+d[1]+','+d[2]+','+d[3]+','+d[4]+','+d[5]+'\n')
# print(stock_data)	


		