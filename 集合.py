#{}为空定义出来的是字典，{}有内容定义出来的是集合
# a ={}#a为字典
# b = {1}#为集合
# c =set()#c为集合
# print(type(a))
# print(type(b))
# print(type(c))
# '''
# 集合的长度
# '''
# print(len(b))
# print(len(c))
'''
集合的并集
'''
# a = {1,2,3}
# b = {1,4,5}
# print(a.union(b))
'''
集合的交集
'''
# a = {1,2,3}
# b = {1,4,5}
# print(a.intersection(b))
'''
集合的差集，我有你没有
'''
# a = {1,2,3}
# b = {1,4,5}
# print(a.difference(b))
'''
集合添加元素
'''
# a = {1,2,3}
# a.add("a")
# print(a)
'''
集合推导式,求出去重的集合
'''
# print({i for i in "24234235425"})
'''
通过集合去重
'''