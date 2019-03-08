#商管程式設計二第四周上課內容 #股票分析 #老師方法
#step1 : preprocess: remove chinese headline,convert to csv file ,remove all space
#step2 : sort data by stock and then by date
#step3 : prepare market return data
#step4 : for each stock: 
# 1. merge stock return with matket data by date
# 2. run regression
# 3. record the result
import csv
import csvsorter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#compute_model
def compute_model(ylist,sdate,mktret):
	"""ylist : list of stock return 
	   sdate : list of return dates
	   mktret:ｍarket return dictionary"""
	xlist = []
	for i in range(0,len(sdate)):
		xlist.append(mktret[sdate[0]])
	if len(xlist) != len(ylist):
		raise Exception("data len error")
	return simple_reg(xlist,ylist)		  

def simple_reg(xlist,ylist):
	sumx = 0.0
	sumy = 0.0
	sumb1 = 0.0
	sumb2 = 0.0
	for i in range(len(xlist)):
		sumx += xlist[i]
		sumy += ylist[i]
	avgx = sumx/len(xlist)	
	avgy = sumy/len(ylist)
	for i in range(len(xlist)):
		sumb1+= (xlist[i]-ylist[i])-(len(xlist)*avgx*avgy)
		sumb2+= xlist[i]**2-(len(xlist)*(avgx**2))
	b = sumb1/sumb2 #目前ok
	a = avgy-(b*avgx)	
	return a,b


#讀檔案
stockfn =  "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock.txt"
fh1 =  open(stockfn,'r',encoding='cp950',newline = '')
cheader = fh1.readline()
reader1 = csv.reader(fh1,delimiter ='\t')
#寫檔案
stockfn_tmp1 = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock_c.csv"
fh3 = open (stockfn_tmp1,'w',encoding='utf-8',newline='') 
writer3 = csv.writer(fh3)
fh3.write('COID,Name,MDATE,ROI,MV,CLOSE\n') #寫入標題
for arow in reader1:
	arow = map(lambda x: x.strip(),arow)
	writer3.writerow(arow)
fh3.close()
fh1.close()		

#把剛剛的檔案按照股票及日期 做排序
stockfn_tmp1 = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock_c.csv"
stockfn_sorted = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock_sorted.csv"
csvsorter.csvsort(stockfn_tmp1,[0,2],output_filename = stockfn_sorted,has_header = True)
#把市場報酬率的資料 加進字典
mktfn = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\market.csv"
fh1 = open(mktfn,'r',newline = '')
reader1 = csv.DictReader(fh1)
mktret = dict()
for arow in reader1:
	mktret[arow['MDATE']] = float(arow['MKT'])
fh1.close()
print("read %d market return data" % len(mktret))	

#把已經排序好的股票excel 跟市場報酬率做合併
coidlist = []
namelist = []
alphalist = []
betalist = []
fh4 = open(stockfn_sorted,'r',encoding = 'utf-8',newline = '')
reader2 = csv.DictReader(fh4)
sret = [] #股票報酬
sdate = [] #股票報酬對應的日期
last_coid= "" #紀錄目前股票代碼
minlen = 2
for arow in reader2:
	this_coid = arow['COID'].strip()
	this_name = arow['Name'].strip()
	if (this_coid) != last_coid:
		if (len(sret)>minlen):
			print('run refressin for COID :' ,last_coid)
			out1 = compute_model(sret,sdate,mktret)
			coidlist.append(last_coid)
			namelist.append(last_name)
			alphalist.append(out1[0])
			betalist.append(out1[1])
		#回歸分析
		sret = [float(arow['ROI'].strip())]
		sdate = [arow['MDATE'].strip()]
	else:
		sret.append(float(arow['ROI'].strip()))		
		sdate.append(arow['MDATE'].strip())
	last_coid = this_coid	
	last_name = this_name
if(len(sret) > minlen):
	print('run refressin for COID :' ,last_coid)
	out1 = compute_model(sret,sdate,mktret)
	coidlist.append(last_coid)
	namelist.append(last_name)
	alphalist.append(out1[0])
	betalist.append(out1[1])
fh4.close()	

#畫圖
ChineseFont2 = FontProperties(fname = 'C:\\Windows\\Font\\mingliu.tcc')
fig,ax = plt.subplots()
ax.scatter(betalist,alphalist)
for i,txt in enumerate(coidlist):
	ax.annotate(txt,(betalist[i],alphalist[i]))
ontproperties = ChineseFont2
plt.show()	
# print(betalist)