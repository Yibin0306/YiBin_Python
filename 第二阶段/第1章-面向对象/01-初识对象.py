"""
1.在程序中设计表格，我们称之为：设计类（class）
class student:
    name = None

2.在程序中打印生产表格，我们称之为创建对象：创建对象
基于类创建对象
stu_1 = student()
stu_2 = student()

3.在程序中填写表格，我们称之为：对象属性
stu_1 = "cyb"  # 为学生1赋予名称属性值
stu_2 = "xjl"  # 为学生2赋予名称属性值
"""

# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建一个对象
stu_1 = Student()

# 对象属性进行赋值
stu_1.name = "cyb"
stu_1.gender = "man"
stu_1.nationality = "china"
stu_1.native_place = "luoyang"
stu_1.age = 18

# 获得对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)





