"""
函数和方法的形参类型注解语法：
def 函数方法名（形参名：类型，形参名：类型，....）
    pass

同时，函数的返回值也是可以添加类型注解的，语法如下
def 函数方法名（形参：类型，形参：类型，....）-> 返回值类型：
    pass
"""

# 对形参进行类型注解
def add(x:int,y:int):
    return x + y
add(1,2)

# 对返回值进行类型注解
def func(data:list) -> list:
    return data
func()