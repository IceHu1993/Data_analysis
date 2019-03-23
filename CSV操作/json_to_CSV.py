import json
import csv

#需求：将 json中的数据转换成csv文件
    #1.分别读json文件，创建csv文件
json_fp = open("list3.json","r")
csv_fp = open("csv.csv","w")
    #2.提取 表头，表内容
data_list = json.load(json_fp)

sheet_title = data_list[0].keys() #dict对象的keys()方法，返回所有Key的值的list
print(sheet_title)
print(type(sheet_title))
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())  #dict对象的values()方法，返回所有value的值的list
    print(type(data.values()))
print(sheet_data)
    #3.创建csv写入器对象
writer = csv.writer(csv_fp)

    #4.写入表头
writer.writerow(sheet_title)
    #5.写入内容
writer.writerows(sheet_data)
    #6.关闭两个文件
json_fp.close()
csv_fp.close()
