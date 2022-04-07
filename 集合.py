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

#列表推导式
print({i for i in 'hogwarts' if i in 'hello word'})