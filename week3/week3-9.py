#商管程式設計二第三周上課內容 #檔案讀取
#在 win裡 \為跳脫字元
#讀取檔案
# file = "f:\\ptt.txt"
# print(file)
# file = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week3\\p.txt"
# file1 = open (file,'r',encoding = 'utf-8')
# linecount = 0
# for line in file1:
# 	linecount+=1
# 	if len(line)<75:
# 		print("%0.2d:%s" % (linecount,line.strip()))
# 	else:
# 		print("%0.2d %s...(truncated)" % (linecount,line[0:75]))	
# file1.close()		

#寫入檔案
file = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week3\\write.txt"
name = input('enter name :')
bir = input('enter birth :')
file2 = open(file,'w',encoding='utf-8')
file2.write(name+'\n')
file2.write(bir+'\n')
file2.close()
