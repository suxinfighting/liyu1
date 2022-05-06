class Person:
    #类变量
    name = 'default'
    age = 0

    def __init__(self, name):
        '''
        构造函数，实例化对象时就调用了
        初始化操作，放在这里
        '''
        self.name = name  # 实例变量
    @classmethod
    def play(self):
        print("playing")

    def jump(self):
        print("jumping")


zs = Person("张三")  # 实例化对象
print(f"zs的姓名是{zs.name}")

#   类变量
print(Person.name)
#   实例变量
print(zs.name)

Person.name = "tom"
zs.name = "lily"
print(Person.name)
print(zs.name)

Person.play()
zs.play()