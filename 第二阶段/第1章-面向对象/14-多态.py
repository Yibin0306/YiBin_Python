"""
多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
多态常作用在继承关系上
比如：
函数形参声明接收父类对象
实际传入父类的子类对象进行工作
即：
以父类做定义声明
以子类做实际工作
用以获得同一行为，不同状态

抽象类（接口）：含有抽象方法的类称之为抽象类
抽象方法：方法是空实现的（pass）称之为抽象方法
"""
# 多态
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('wang')

class Cat(Animal):
    def speak(self):
        print('miao')

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_1_r(self):
        """左右摆风"""
        pass

class MeiDi_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")
    def hot_wind(self):
        print("美的空调核心制热科技")
    def swing_1_r(self):
        print("美的空调左右摆风")

class GeLi_AC(AC):
    def cool_wind(self):
        print("格力空调核心制冷科技")
    def hot_wind(self):
        print("格力空调核心制热科技")
    def swing_1_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

meidi = MeiDi_AC()
geli = GeLi_AC()
make_cool(meidi)
make_cool(geli)