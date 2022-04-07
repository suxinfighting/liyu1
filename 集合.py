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