"""
函数本身，也可以作为参数传入另一个函数内
是一种计算逻辑的传递，而非数据的传递
任何逻辑都可以自行定义并作为函数传入
"""

# 列子
def test_func(compute):
    result = compute(1,2)
    print(f"compute的参数类型是{type(compute)}")
    print(result)

def compute(x,y):
    return x + y

test_func(compute)