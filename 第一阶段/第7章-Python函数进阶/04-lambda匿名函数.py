"""
函数的定义中
def关键字，可以定义带有名称的函数
lambda关键字，可以定义匿名函数（无名称）
有名称的函数，可以基于函数名称重复使用
无名称的匿名函数，只可以临时使用一次

匿名函数定义语法：
lambda 传入参数: 函数体（一行代码）
lambda是关键字，表示定义匿名函数
传入参数表示形式参数
函数体表示函数的执行逻辑，但是只能写一行，无法写多行代码
"""

def test_func(compute):
    result = compute(1,2)
    print(result)

test_func(lambda x,y: x+y) # lambda默认return值