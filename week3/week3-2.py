#商管程式設計二第三周上課內容 #身分證驗證 用tuple zip功能
def verify_id(idstr):
	"""verify taiwan id number"""
	#check len
	if len(idstr)!=10:
		return False
	# check first letter
	code1 = ord(idstr[0]) #把idstr的第0個index的字的編碼回傳 ex A 回傳編碼為65 (ASCII)
	if (code1<65  or code1>90):
		return False
	#check remianing letter
	for i in range(1,10):
		code2 = ord(idstr[i])
		if (code2<48 or code2>57):
			return False
	#check the second character
	code2 = ord(idstr[1])
	if (code2<49 or code2>50):
		return False

	cmap = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33] 
	weight = [1,9,8,7,6,5,4,3,2,1,1]
	checksum = 0
	
	num1 = cmap[code1-65] #把第一個英文轉成數字
	newid = str(num1)+idstr[1:]
	print("newid = " ,newid )

	for pair in zip(newid,weight): #checksum 的驗證方法
		print(pair)
		checksum+=int(pair[0])*pair[1]
	remainder = checksum % 10
	if remainder ==0:
		return True
	else:
		return False

			


idstr = "N225959124"
print(verify_id(idstr))
