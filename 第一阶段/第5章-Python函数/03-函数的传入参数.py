"""
函数的定义语法：
def 函数名(传入参数):
    函数体
    return 返回值

传入参数：在函数进行计算时，接受外部(调用时)提供的数据
"""

# 例子
def add(x,y):
    result = x + y
    print(f"{x}+{y}的结果是：{result}")
num1 = int(input("输入第一个数:"))
num2 = int(input("输入第二个数:"))
add(num1,num2)

"""
上述代码中x和y为形式参数（形参）。其中可以不使用参数，也可以使用任意N个参数
参数之间用逗号进行分隔

提供的num1和num2为实际参数（实参）
传入时候，按照顺序传入参数，使用逗号进行分隔
"""

# 练习
def temperature (num):
    print("请出示您的健康码以及72小时核酸证明，并配合测量体温。")
    if num <= 37.5:
        print(f"您的温度是{num}度数,体温正常请进。")
    else:
        print(f"您的温度是{num}度数,需要隔离。")
temperature(int(input("请输入温度:")))