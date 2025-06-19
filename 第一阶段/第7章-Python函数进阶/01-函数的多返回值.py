# 函数多返回值
def test_return():
    return 1,2
x,y = test_return()
print(f"第一个返回值是{x}，第二个返回值是{y}")