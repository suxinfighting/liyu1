'''
创建元组
'''
# 1.逗号分割
tup1 = 1, 2, 3
print(type(tup1),tup1)

# 小括号填充元素
tup2 = (1, 2, 3)
print(type(tup2), tup2)

# 构造函数tuple
tup3 = tuple()
print(type(tup3), tup3)
# 字符串
tup4 = tuple('hogwarts')
print(type(tup4), tup4)
# 列表
tup5 = tuple([1, 2, 4])
print(type(tup5), tup5)

tup6 = 1,
tup7 = (2,)
print(type(tup6), tup6)
print(type(tup7), tup7)

tup8 = 1
tup88 = (2)
print(type(tup8), tup8)
print(type(tup88), tup88)

'''
元组索引
'''
tup9 = 'hogwarts'
# 1.正向索引
print(tup9[2])

# 2.反向索引
print(tup9[-1])
'''
元组切片
'''
# tup10 = tuple('hogwarts')
# print(tup10)
# # 获取前三个元素
# print(tup10[:3])
# # 反转元组
# print(tup10[::-1])

'''
元组方法-index
'''
tup11 = tuple('hogwarts')
print(tup11.index('o'))
print(tup11.index('x'))
print(tup11.count('o'))
'''
元组定义
'''
# tuple1 = (1,2,3)
# tuple2 = 1,2,3
# print(tuple1)
# print(tuple2)
'''
元组不可变
'''
# tuple1 = (1,2,3)
# tuple1[0] = "a"
'''
元组不可变,但元组中有列表，列表的元素可变
'''
# a = [1,2,3]
# tuple1 = (1,2,a)
# tuple1[2][0] = "a"
# print(tuple1)
'''
查询某个元素在元组中出现几次
'''
# tuple1 = (1,2,3)
# print(tuple1.count(2))
'''
求对应元素的索引
# '''
# tuple1 = (1,2,3)
# print(tuple1.index(2))
