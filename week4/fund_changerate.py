import csv
#讀檔案
with open('fund_changerate.txt','r',encoding = 'cp950',newline = '') as file:
	header = file.readline()
	read_file = csv.reader(file,delimiter= ',')
	#寫檔案
	with open('fund_changerate.csv','w',encoding = 'cp950',newline = '') as file_csv :
		write_file = csv.writer(file_csv)
		file_csv.write('基金碼,簡稱,年月日,近一年變動率%\n') #寫入標題
		data = []
		for arow in read_file:
			print(arow)
			convert_rate = arow[3].strip()
			if convert_rate == '-':
				arow[3] = -1000000000
			else:
				arow[3] = float(arow[3])
			data.append(arow)	
		data.sort(key=lambda x:x[3],reverse=True)  #逆序	 #資料按照報酬率排序
		for d in data:
			write_file.writerow(d)	
		# print(data)
		

