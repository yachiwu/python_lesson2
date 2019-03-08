#商管程式設計二第三周上課內容 #python 特別有的函數
# def f1(x):
# 	return x**2
# print(f1(8))	
# #用lambda 函數
# f2 = lambda x : x**2
# print(f2(8))
#zip 函數
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
tuple_zip = tuple(zipped)
print(type(tuple_zip[0][0]))
# #搭配map函數 可以重複執行某個函數
# list1 = [3,5,2,4,9]
# #要讓list裡面的每個東西都平方 
# out1 = map(f1,list1)
# print(list(out1))
# out2 = map(lambda x: x**2,list1)
# print(list(out2))
# # print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
