#商管程式設計二第三周上課內容 #set 
#set 裡面東西不會重複
#set 是 immutable(傳值)
aset = {11,22,33}
bset = aset
aset = aset | {55}
print('aset',aset)
print('bset',bset)
#set 沒有set[0] 這種用法 也沒有+ 這種字串相加的用法
alist = ['you','me','his','you']
aset = set(alist)
print(aset) 
#輸出 {'me', 'his', 'you'} set會自動把重複的value刪除

#set可以做
set1 = {11,22,33,60}
set2 = {22,55,60}
print(set1|set2) #交集
#輸出{33, 22, 55, 11, 60}
print(set1 & set2) #聯集
# 輸出 {60, 22}
print(set1 - set2) #差集
# 輸出 {33, 11}
print(set1 ^ set2) #symmetric difference
#有在a沒有在b 或有在b沒有在a
# 輸出 {33, 11, 55}