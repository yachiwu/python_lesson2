#商管程式設計二第三周上課內容 #mutable 跟 immutable 的差別
#python 中 mutable 是可以改變值(用的方式為傳參)
#ex. list
# a = [1,2,3]
# b = a
# a.append(4)
# print(a)
# print(b)
# ##python 中 immutable 是不可以改變值(用的方式為傳值)
# # ex. str , tuple
# my_tuple = (3,2,1)
# saved = my_tuple
# my_tuple+=(44,)
# print(my_tuple)
# print(saved)  #結果為saved沒有被改變 為加上44原因為tuple的資料結構為傳值 在 saved = my_tuple時 my_tuple裡面的值只有(1,2,3)

# #tuple 本身沒有排序的function 
# #所以不能寫 tuple.sort()
# #但是可以寫成 
# atuple = sorted(my_tuple)
# print(atuple)  #return a list!

# #tuple跟list類似的地方
# print(len(my_tuple))
# print(44 in my_tuple)

# #tuple 跟list 互相轉換
# alist = [11,22,33]
# my_tuple = tuple(alist)
# print(my_tuple)

# #tuple 跟字串轉換
# newtuple = tuple('hello world !')
# print(newtuple)

#tuple 的功能一 zip
id = '123456'
weight = [6,5,4,3,2,1]
for pair in zip(id,weight):
	print(pair)