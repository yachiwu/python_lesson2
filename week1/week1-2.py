# #商管程式設計二第一周上課內容 #recursion 遞迴
# 0! = 1
# n! = n * (n-1)!

def factorial(n):
	space = ' ' *(4*n)
	print(space,'factorial',n)
	if not isinstance(n,int):
		print('factorial is only defined for integers')
		return None
	elif n<0:
		print('factorial is only defined for negative values')
		return None
	elif n == 0:
		print(space,'returning 1 ')
		return 1
	else:
		recurse = factorial(n-1)	
		result = n*recurse
		print(space,'factorial',result)
		return result
print(factorial(4))		