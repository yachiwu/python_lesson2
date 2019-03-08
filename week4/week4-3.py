#商管程式設計二第四周上課內容 #將市場報酬率存入字典
import csv
mktfn = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\market.csv"
fh1 = open(mktfn,'r',newline = '')
reader1 = csv.DictReader(fh1)
mktret = dict()
for arow in reader1:
	mktret[arow['MDATE']] = float(arow['MKT'])
fh1.close()
print("read %d market return data" % len(mktret))	
print(mktret['20180314'])