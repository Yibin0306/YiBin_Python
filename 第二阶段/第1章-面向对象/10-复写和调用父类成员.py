"""
复写：子类继承父类的成员属性和成员方法后，如果对其不满意，那么可以进行复写
即：在子类中重新定义同名的属性或方法即可

调用父类同名成员：一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
如果需要使用被复写的父类的成员，需要特殊的调用方式
方式一：
使用成员变量：父类名.成员变量
使用成员方法：父类名.成员方法（self）
方式二：使用super（）调用父类成员
使用成员变量：super（）.成员变量
使用成员方法：super（）.成员方法（）
"""

# 复写
class Phone:
    producer = 'XiaoMi' #厂商
    def call_by_4g(self):
        print('使用4G通话')

class MyPhone(Phone):
    producer = 'Iphone' #复写
    def call_by_4g(self): #复写
        # 在子类中，调用父类同名成员
        # 方式一
        print(f'父类的厂商是{Phone.producer}')
        Phone.call_by_4g(self)
        # 方式二
        print(f'父类的厂商是{super().producer}')
        super().call_by_4g()


phone = MyPhone()
phone.call_by_4g()
print(phone.producer)

