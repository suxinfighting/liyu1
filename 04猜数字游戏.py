'''
计算机给出一个随机数
人去猜
'''


import random

computer_num = random.randint(1,100)
people_num = int(input("请输入数字"))

while True:
    if people_num<computer_num:
        print("猜小了")
        people_num = int(input("请输入数字"))
    elif people_num>computer_num:
        print("猜大了")
        people_num = int(input("请输入数字"))
    else:
        print("猜对了")
        break