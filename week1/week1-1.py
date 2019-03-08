# #商管程式設計二第一周上課內容 #five littile duck  #function

#版本一
def over_mother():
	print("Over the hills and far away")
	print("Mother duck said quack quack quack")
def n_duck(num):
	print("%s litte ducks went out day" % num)
def only_n(num):
	print("But only %s little ducks came back" % num)

# n_duck("Five")
# over_mother()
# only_n("Four")		
# print()
# n_duck("Four")
# over_mother()
# only_n("Three")		
# print()
# n_duck("Three")
# over_mother()
# only_n("Two")		
# print()
# print("end")

#版本二 更精簡
def sing_unit(num1,num2):
	n_duck(num1)
	over_mother()
	only_n(num2)

sing_unit("Five","Four")
print()	
sing_unit("Four","Three")
print()	
sing_unit("Three","Two")