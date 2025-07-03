"""
基于类创建对象的语法：对象名 = 类名称()
类只是一种程序内的设计图纸，需要基于图纸生产实体(对象)，才能正常工作
这种思想，称之为，面向对象编程
"""

# 设计一个闹钟类
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 创建两个闹钟对象并让其工作
clock = Clock()
clock.id = "001"
clock.price = 9.9
print(f"闹钟ID：{clock.id}，闹钟价格：{clock.price}")
clock.ring()