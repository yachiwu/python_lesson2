#商管程式設計二第四周上課內容 #股票分析 #排序csv檔 先用股票代碼排序再用日期
import csvsorter
stockfn_tmp1 = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock_c.csv"
stockfn_sorted = "C:\\Users\\Master\\Desktop\\大學 課程\\python 商管程式設計 台大MOOC (二)\\上課練習檔案\\week4\\stock_sorted.csv"
csvsorter.csvsort(stockfn_tmp1,[0,2],output_filename = stockfn_sorted,has_header = True)