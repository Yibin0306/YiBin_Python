"""
变量作用域指的是变量的作用范围
主要分为两类：局部变量和全局变量

局部变量：定义在函数体内部的变量，即只在函数体内部生效
作用：在函数体内部，临时保存数据，当调用完成立刻销毁局部变量

全局变量：在函数体内、外都能生效的变量

global关键字
作用：可以在函数内声明变量成全局变量
"""

# 局部变量
def test_a():
    number = 100
    print(number)
test_a()# 100正常输出
# print(num) 会报错num未定义

# 全局变量
num = 100
def test_b():
    print(num)
def test_c():
    print(num)
test_b()
test_c()

# 在函数内修改全局变量
a = 100
def func_a():
    print(f"func_a是{a}")
def func_b():
    global a # 声明a是全局变量
    a = 200 # 局部变量成全局变量
    print(f"func_a是{a}")
func_a()
func_b()
print(a)