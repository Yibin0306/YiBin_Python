"""
一个函数里面又调用了另一个函数
"""

def func_b():
    print("---2---")

def func_a():
    print("---1---")
    # 调用func_b
    func_b()
    print("---3---")

func_a()