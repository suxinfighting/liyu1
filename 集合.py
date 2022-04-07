'''
创建集合
'''
# * 通过使用{}填充元素
set1 = {1, 2, 3}
print(type(set1), set1)
# * 通过构造方法 set()
# 字符串
set2 = set("hogwarts")
print(type(set2), set2)
# 列表
set3 = set([1, 2, 3])
print(type(set3), set3)

# 创建空集合
set4 = set()
print(type(set4), set4)
# * 通过集合推导式
set5 = {i for i in range(1,11) if i % 2 == 0}
print(type(set5), set5)


'''
成员检测
'''
set6 = {1, 2, 3, 4}
print(1 in set6)
print(100 not in set6)

'''
集合方法
'''

# add
set7 = set()
# set7.add(1)
# set7.add(2)
# set7.add('asdas')
set7.update('hogwarts')
print(set7)
# 传入列表
set7.update([1, 2, 3])
print(set7)

'''
remove
'''
set8 = {1, 2, 'hogwarts'}
# set8.remove(1)
# print(set8)
#
# set8.remove(100)
'''
discard(item)
移除元素
'''
# # 1.元素存在
# set8.discard(1)
# print(set8)
#
# # 2.元素不存在
# set8.discard(100)


'''
pop()
'''
# set9 = {1, 2, 'hogwarts'}
# set9.pop()
# print(set9)

'''
clear
'''
# set10 = {1, 2, 3, 4}
# set10.clear()
# print(set10)

'''
集合运算
'''
# 交集
a = {1, 2, 3}
b = {1, 4, 5}
# print(a.intersection(b))
# print(a & b)
#
# # 并集
# print(a.union(b))
# print(a | b)

#差集
print(a.difference(b))
print(a - b)

'''
列表推导式
示例：寻找hogwarts与hello word的共同字母
'''

# for循环
set10 = set()
for i in 'hogwarts':
    if i in 'hello word':
        set10.add(i)
print(set10)

# 列表推导式
print({i for i in 'hogwarts' if i in 'hello word'})




