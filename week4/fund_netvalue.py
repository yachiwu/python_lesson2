def read_file(filename):
	fundlist = []
	with open(filename,'r',encoding= 'cp950') as f:
		for line in f:
			if '基金碼	簡稱	年月日	幣別	淨值(元)' in line:
				continue
			else:
				fundlist.append(line.strip().split())
	return fundlist		
				
def write_file(filename,fundlist):
	with open(filename,'w',encoding = 'utf-8') as f:
		f.write('簡稱,日期,淨值\n')
		for data in fundlist:
			f.write(data[1]+','+data[2]+','+data[4]+'\n')
def find_data(fundlist):
	date = []
	netvalue = []
	for data in fundlist:
		date.append(data[2])
		netvalue.append(float(data[4]))
	return date ,netvalue
def picture(date,netvalue):
	import matplotlib.pyplot as plt	
	from matplotlib.font_manager import FontProperties
	fig = plt.figure()		 #定義一個圖像窗口
	plt.plot(date,netvalue)
	plt.title('T0903Y Fund Net Value from 0211~0306')
	plt.show()
	fig.savefig('fund.png')
	

def main():
	fundlist = read_file('fund net value.txt')	
	write_file('fund net value.csv',fundlist)
	# print(fundlist)
	date,netvalue = find_data(fundlist)
	# print(date)
	# print(netvalue)
	picture(date,netvalue)
	

main()	