"""
内置的类方法，各自有各自特殊的功能，这些内置方法我们称之为：魔术方法
__init__()方法，称之为构造方法
__str__()方法，称之为字符串方法
__lt__()方法，称之为小于，大于符号比较
__le__()方法，称之为小于等于、大于等于符号比较
__eq__()方法，称之为==符号比较
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__()方法
    def __str__(self):
        return f"Student {self.name} is {self.age} years old." # 不写输出的直接是内存地址

    # __lt__()方法
    def __lt__(self,other):
        return self.age < other.age

    # __le__()方法
    def __le__(self,other):
        return self.age <= other.age

    # __eq__()方法
    def __eq__(self,other):
        return self.age == other.age

stu1 = Student("cyb",18)
stu2 = Student("xjl",17)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 == stu2)