#商管程式設計二第三周上課內容 #dictionary
eng = dict()

# eng = {}
# print(eng)
# print(type(eng))
eng['one'] = '一'
eng['two'] = '二'
eng['three'] = '三'
eng['four'] = '四'
print(eng)
#用key 來找value
# if 'one' in eng: #這邊的in 是在找在eng這個字典裡沒有one 這個key!!!!
# 	print(eng['one'])
# print(eng.get('three'))
print(eng.keys())
print(eng.values())
#跑出結果
# dict_keys(['one', 'two', 'three', 'four'])
# dict_values(['一', '二', '三', '四'])
print(eng.items())
#dict_items([('one', '一'), ('two', '二'), ('three', '三'), ('four', '四')])