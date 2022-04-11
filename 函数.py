# # 定义函数
# def func_demo():
#     # 函数体
#     print("这是一个函数")
#
# def func_with_params(a, b, c):
#     '''
#     这是一个携带参数和注释的函数
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     '''
#     print("这是一个携带参数和注释的函数")
#
# # 打印函数注释法一
# print(func_with_params.__doc__)
#
# # 打印函数注释法二
# help(func_with_params)
#
# # 定义空函数
# def filter_char():
#     pass
#
# # 调用函数
# func_demo()
# func_with_params(1, 2, 3)
#
# def demo2(a, b, c=[]):
#     c.append(a)
#     c.append(b)
#     print(a, b, c)
#
#
# (demo2(1, 2))
# (demo2(3, 4))

'''
args
不知道有多少参数会传进来，期望传进来的参数都可以被接收
'''


def print_language(*args):
    # print(args)
    for i in args:
        print(i)


# 调用函数，把不同数量的参数传递进去
# print_language('python', 'java')
# print_language('python', 'java', 'go')
# lan = ['python', 'java', 'go']
# print_language(lan)
# print_language(*lan)
'''
kwargs
'''


def print_info(**kwargs):
    print(kwargs)


# print_info(Tom=18, Lily=12)
# print_info(Tom=18, Lily=12, Anna=16)

# 直接传入字典
data = {
    "Tom": 18,
    "Lili": 12,
    "Anna": 16
}
print_info(**data)  # 解包
