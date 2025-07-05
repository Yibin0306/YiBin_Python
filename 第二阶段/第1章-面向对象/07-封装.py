"""
面向对象编程，是许多编程语言都支持的一种思想
简单理解就是：基于模板（类）去创建实体（对象），使用对象完成功能开发

面向对象有三大主要特性：封装、继承、多态
封装到类中，描述为：成员变量、成员方法

类中提供了私有成员的形式来支持
    私有成员变量
    私有成员方法
定义私有成员的方式，只需要：
    私有成员变量：变量名以__开头
    私有成员方法：方法名以__开头

私有成员，对象无法使用，但是类内可以调用
在类中提供仅供内部使用的属性和方法，而不对外开放(类对象无法使用)
"""
class Phone:
    __current_voltage = 0.5 # 手机电压

    def __keep_single_core(self):
        print("让cpu以单核运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，已设置为单核模式运行进行省电")

phone = Phone()
phone.call_by_5G()