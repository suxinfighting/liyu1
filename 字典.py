'''

创建字典
'''
# 1.大括号键值对填充
# 有值
# dic1 = {"name": "herry", "age": "18"}
# print(type(dic1), dic1)
# 创建空字典
# dic2 = {}
# print(type(dic2), dic2)

# 2.构造方法dict
# 创建空字典
# dic3 = dict()
# print(type(dic3), dic3)
# 创建非空字典
# dic4 = dict([("name", "herry"), ("age", 18)])
# print(type(dic4), dic4)

# # 3.字典推导式创建
# dic5 = {k: v for k, v in [("name", "herry"), ("age", 18)]}
# print(type(dic5), dic5)

'''
字典使用：访问元素
'''
# # 访问存在的key
# dic6 = {"name": "herry", "age": "18"}
# print(dic6["name"])
# # 访问不存在的key
# # print(dic6["hobby"])
#
# # 修改字典的value值
# dic6["age"] = 20
# print(dic6)

# # 添加元素
# dic6["hobby"] = "magic"
# print(dic6)
#
# """字典使用：嵌套字典"""
# dc = {"name": "Harry Potter", "age": 18, "course": {"magic": 90, "python": 80}}
# # 1、获取课程Magic的值
# print(dc['course']['magic'])
#
# # 2、把python分数改成100分
# dc['course']['python'] = 100
# print(dc)

'''
字典方法
'''
# keys、values、items
# dic7 = {"name": "herry", "age": "18"}
# print(dic7.keys(), type(dic7.keys()))
# print(dic7.values(), type(dic7.values()))
# print(dic7.items(), type(dic7.items()))

# 转成列表
# print(list(dic7.keys()))
# print(list(dic7.values()))
# print(list(dic7.items()))

'''
get
'''
# dic8 = {"name": "herry", "age": "18"}
# # 1.访问存在的key
# print(dic8.get("name"))
# # 2.访问不存在的key
# print(dic8.get('hobby'))

'''
update
'''
# dic9 = {"name": "herry", "age": "18"}
# dic9.update({'age': 20, 'hobby': 'magic'})
# print(dic9)

'''
pop
# '''
# dic10 = {"name": "herry", "age": "18"}
# # 1.移除已经存在的key
# print(dic10.pop('name'))
# print(dic10)
# # 2.移除不存在的key
# # dic10.pop('bohhy')

'''
字典推导式

'''
# 示例1
dic11 = {k: v for k,v in [("name", "herry"), ("age", 10)]}
print(dic11)

# 示例2
'''
实例：给定一个字典对象{'a': 1, 'b': 2, 'c': 3}，找出其中所有大于 1 的键值对，同时 value 值进行平方运算。
'''
# for循环
dic12 = {'a': 1, 'b': 2, 'c': 3}
data = dict()
for k, v in dic12.items():
    if v > 1:
        data[k] = v ** 2

print(data)

# 字典推导式
print({k: v ** 2 for k, v in {'a': 1, 'b': 2, 'c': 3}.items() if v > 1})

'''
给定一个字典对象，请使用字典推导式，将它的key和value分别进行交换。也就是key变成值，值变成key。

输入: {'a': 1, 'b': 2, 'c': 3}
输出: {1: 'a', 2: 'b', 3: 'c'}
'''
dic13 = {'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in dic13.items()})