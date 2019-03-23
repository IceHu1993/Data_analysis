import json

#1.字符串和 dict list转换
    #字符串------> dict、list
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(data)
print(type(data))
print(type(list_data))
    #dict、list----->字符串
list2 = [{"name":"张三","age":20},{"name":"李四","age":18}]
str_data = json.dumps(list2)
print(type(str_data))

#2.文件对象和 dict 、list转换
    #dict、list----->文件对象
list3 = [{"name":"张三","age":20},{"name":"李四","age":18}]
json.dump(list3,open("list3.json","w"))
    #json文件对象----->list、dict
json_file = open('list3.json','r')
json_list = json.load(json_file)
print(json_list)

