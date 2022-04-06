'''
创建列表
'''
# 1.构造方法list()
li = list()
print(type(li), li)
li1 = list("hogwarts")
print(type(li1),li1)
# 2.中括号[]创建并填充
li2 = [2, 3, 45, 6]
li3 = ["hogwarts", "hello"]
li4 = [3, 4.2, "asd", [3, 4, 5]]
print(li2)
print(li3)
print(li4)
# 3.列表推导式
li5 = [i for i in range(1,10) if i%2 == 0]
print(type(li5),li5)
'''
列表使用-索引
'''
li6 = [1,2,3,4,5]
# 1.正向索引
print(li6[2])
# 2.负向索引
print(li6[-3])
'''
列表使用-运算符
'''
# 1.*号
li7 = [1]
print(li7*5)

# 2.+号
li8 = [1,2,3]
li9 = [4,5,6]
print(li8 + li9)

'''
列表使用-成员检测
'''
li10 = [1, 2, 3]
print(1 in li10)
print(100 in li10)

print(1 not in li10)
print(100 not in li10)

'''
列表方法
'''
# append
li11 = []
li11.append(1)
li11.append("hog")
print(len(li11), li11)

# extend
li12 = ['a', 'b', 'c']
li12.extend('hello')
print(len(li12), li12)

# insert
li13 = [1,2,3]
li13.insert(0,'hogwarts')
print(li13)
li13.insert(2,'hello')
print(li13)

# pop
li14 = [1, 2, 3, 4, 5]
data = li14.pop()
print(data, li14)
data1 = li14.pop(1)
# print(data1, li14)
# li14.pop(99)
# li15 = []
# li15.pop()

# remove
li16 = ['a', 'b', 'c']
li16.remove('c')
# print(li16)
# li16.remove('d')

# sort
# li18 = [1, 4, 6, 2, 9, 5]
# li18.sort()
# print(li18)
# li18.sort(reverse=True)
# print(li18)
# li19 = ['java', 'python', 'go', 'R']
# li19.sort(key=len)
# print(li19)

# reverse
li20 = ['a', 'b', 'c']
li20.reverse()
print(li20)

li21 = [1,2,3]
print(li21[::-1])

'''
列表嵌套
'''
# li21 = [[1, 2, 3], ['a', 'b', 'c']]
# # 获取b
# print(li21[1][1])
# # c后追加d
# li21[1].append('d')
# print(li21)

'''
列表推导式
实例：将 1-10 中的所有偶数平方后组成新的列表
'''
# 传统for循环
# result = []
# for i in range(1,11):
#     if i % 2 == 0:
#         result.append(i**2)
# print(result)
#
# # 列表推导式
# result2 = [i**2 for i in range(1,11) if i % 2 == 0]
# print(result2)

'''
list.append(x)，在列表末尾添加一个元素
list.insert(i,x),在i处插入一个元素
list.remove(x),移除第一个值为x的元素，如果没有这样的元素，就抛出ValuError异常
list.pop(i),删除列表中给定位置的元素并返回它；如果没有给定位置，会自动删除并返回最后一个元素;如果位置超出，会抛出IndexError
list.sort(),默认升序排序；参数reverse=True时，降序排序
list.reverse(),反转列表
'''
# list1 = [1, 2, 'x', 3, 4]
# list1.append(0)
# print(list1)
# list1.insert(2,'x')
# print(list1)
# list1.remove(2)
# print(list1)
# print(list1.pop(10))
# print(list1)
# list1 = [4,2,1,6,8]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# list1 = [4,2,1,6,8]
# list1.reverse()
# print(list1)

# list1 = [4,2,1,6,8]
# list1[5]=9
# print(list1[1:])
# list1 = [4,2,1,6,8]
# print(list1[::-1])
# list1 = [4,2,1,6,8]
# print(list1[1:3])

'''
生成平方列表，比如【1，4，9】
分别用for循环、列表推导式
'''
# list_square = []
# for i in range(1,4):
#     list_square.append(i**2)
# print(list_square)
#
# list_square2 = [i**2 for i in range(1,4)]
# print(list_square2)
#
# list_square3 = [i**2 for i in range(1,4) if i!=1]
# print(list_square3)
#
# list_square4 = [i+i if i ==1 else i**2 for i in range(1,4)]
# print(list_square4)
#
# list_square5 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_square5)