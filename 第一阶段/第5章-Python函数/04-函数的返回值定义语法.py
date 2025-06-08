"""
函数的定义语法：
def 函数名(传入参数):
    函数体
    return 返回值
变量 = 函数(参数)

return：指完成功能后，会将结果返回给函数调用者
"""

num1 = int(input("输入第一个数:"))
num2 = int(input("输入第二个数:"))
def add(x,y):
    result = x + y
    # 通过返回值，将结果返回给调用者
    return result
    # 执行不到这，上面就返回了
    print("结束了")
# return的返回值，可以通过变量去接收
r = add(num1,num2)
print(r)