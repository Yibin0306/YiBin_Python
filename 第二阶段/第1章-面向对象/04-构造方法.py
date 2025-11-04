"""
python类可以使用:__init__()方法，称之为构造方法

可以实现:
        在创建类对象（构建类）的时候，会自动执行
        在创建类对象（构建类）的时候，将传入参数自动传递给__init__方法使用

注意事项：__init__两个下划线不要忘写
        不要忘记在参数列表中加self
        在构建方法内定义成员变量，需要用self关键字
"""

class Student:

    def __init__(self,name,age,tel):
        self.name = name # 既有赋值功能，也有定义功能
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象") # 证明会自动执行

student = Student("Yibin","18","176297") # 传入参数自动传递给__init__方法
print(f"姓名:{student.name},年龄:{student.age},电话:{student.tel}")