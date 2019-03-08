# #商管程式設計二第二周上課內容 #convert date 
def ymd2dmy(dstr):
	y1 = dstr[0:4]
	m1 = dstr[4:6]
	d1 = dstr[6:8]
	return d1+m1+y1
print(ymd2dmy("20150212"))	
