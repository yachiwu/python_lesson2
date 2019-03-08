#商管程式設計二第三周上課內容 #dictionary 的例子
#計算字串中的每個字母出現幾次 ex a 出現3次等等
def histogram(seq):
	d = dict()
	for element in seq:
		if element in d:
			d[element]+=1
		else:
			d[element] = 1
	return d
#計算字串中 出現n次的字母有哪些 ex 出現三次的有 a,b,c
def invert_dic(d):
	inv = dict()
	for key in d:
		print(key)
		value = d[key]
		if value in inv:
			inv[value].append(key)
		else:
			inv[value] = [key]
	return inv		
#三種印出字典內容方法			
# def print_his(hist):
# 	for key in hist:
# 		print(key,hist[key])	
# def print_his2(hist):
# 	for key,value in hist.items():
# 		print(key,value)		
def print_his3(hist):
	keys = hist.keys()
	for key in sorted(keys):
		print(key,hist[key])
h = histogram('oabcddeeaaa')
print_his3(h)	
print(invert_dic(h))