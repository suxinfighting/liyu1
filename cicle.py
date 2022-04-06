'''
1.1-100求和
'''
result = 0
for i in range(101):
    result = result+i
print(result)
'''
分支结构求1-100偶数的和
'''
result = 0
for i in range(101):
    if i%2 ==0:
        result = result+i
print(result)
'''
python步长求1-100偶数的和
'''
result = 0
for i in range(2,101,2):
    if i%2 ==0:
        result = result+i
print(result)
'''
break
'''
for i in range(1,10):
    print(i)
for i in range(1,10):
    if i == 5:
        continue
    print(i)
for i in range(1,10):
    if i == 5:
        break
    print(i)
'''
猜数字游戏，
计算机给出一个数
人给出一个数
计算机提示：猜大了、猜小了、猜对了
'''
import random
computer_num = random.randint(1,100)
while True:
    person_num = int(input("请输入一个数字"))
    if computer_num>person_num:
        print("猜小了")
    elif computer_num<person_num:
        print("猜大了")
    else:
        print("猜对了")
        break