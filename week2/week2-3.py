#商管程式設計二第二周上課內容 #中文編碼問題
# -*- coding :utf8 -*- 
# msg = '晚上七點水源星巴克見'
# code = ""
# convert =""
# for c in msg:
# 	print(ord(c),end= " ")
# 	code+=str(ord(c))+" "
# print()	
# print(code)

# for c in code.split():
# 	convert+=chr(int(c))
# print(convert)	
s2 ="media,and,mania,and,ia"
print(s2.find('a')) #找出a出現的第一次在第幾個位置
print(s2.isnumeric()) #s2是否為數字
print(s2.count('ia')) #計算ia出現幾次
print(s2.split(',')) #s2以逗點分割 分割後為清單

s3 = "HI I AM CUTE"
print(s3.isupper()) #s3是否全為大寫
print(s3.split()) #s3以空白分割

s4 = "www.example.com"
print(s4.strip('comw.')) #去掉含有 c m o w z .的字
#strip() 去除空白
