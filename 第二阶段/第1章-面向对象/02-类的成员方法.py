"""
类的常用语法：
class 类名称： # class是关键字，表示要定义类了
    类的属性   # 类的属性，即定义在类中的变量（成员变量）
    类的行为   # 类的行为，即定义在类中的函数（成员方法）

创建对象的语法：
对象 = 类名称（）

类中：
不仅可以定义属性用来记录数据
也可以定义函数，用来记录行为
其中：
类定义的属性，称之为：成员变量
类定义的行为，称之为：成员方法

在类中定义函数语法有细微的差别：
def 方法名(self,形参1,....,形参N)
    方法体
其中self是成员方法定义时候，必须填写的
    它是用来表示对象自身的意思
    当我们使用类对象调用的方法是，self会自动被python传入
    在方法内部，想要访问类的成员变量，必须使用self
    self关键字，尽管在参数列表中，但是传参的时候可以忽略它
"""

# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print("Hello, my name is %s" % self.name)

    def say_hello(self, msg):

Student_1 = Student()
Student_1.name = "cyb"
Student_1.say_hi()