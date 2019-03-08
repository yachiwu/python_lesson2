#商管程式設計二第三周上課內容 #例外處理
# x = 1
# try:
# 	inv = 1/x
# except Exception as inst:
# 	inv = 0
# 	print('Exception encountered !')
# 	print(type(inst))
# 	print(inst)
# print('\n === \n inv = %f' %inv)	
# while True:
# 	try:
# 		x = int(input('請輸入數字'))
# 		break
# 	except ValueError:
# 		print('輸入非數字,請重新數入')	
# print('得到數字 : %d ' %x)		
import random
def throwcoin(prob = 0.5):
	if prob>1 or prob<0:
		raise Exception('ellegal probability')
	p = random.random()	
	if p<prob:
		print(p)
		return "亂數輸了"
	else:
		print(p)
		return "亂物贏了"	
print(throwcoin(0.2))