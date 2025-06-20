"""
列如在嵌套函数中，第一个函数有异常，后续函数有调用第一个函数的话，异常具有传递性
"""

# 列子
def func1():
    print("func1开始")
    num = 1/0
    print("func1结束")

def func2():
    print("func2开始")
    func1()
    print("func2结束")

def main():
    try:
        func2()
    except Exception as e:
        print(e)
main()