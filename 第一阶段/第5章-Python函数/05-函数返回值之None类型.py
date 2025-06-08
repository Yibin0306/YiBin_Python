"""
None类型：表示空的、无实际意义的意思
用在函数无返回值上

在if判断上None等于False
一般用在函数中主动返回None，配合if判断做相关处理

用于声明变量上
定义变量，但暂时不需要变量有具体值，可以用None来代替
"""

# 列
# def say():
#     print("hello")
# outcome = say()
# print(f"返回的内容是{outcome}")
# print(f"返回的类型是{type(outcome)}")

# 手动返回None
# def say():
#     print("hello")
#     return None
# outcome = say()
# print(f"返回的内容是{outcome}")
# print(f"返回的类型是{type(outcome)}")

# None用于if判断
def check_age(age):
    if age >= 18:
        return True
    else:
        return None
result = check_age(17)
# if判断条件是true,假设result是None，not result为true，故可以进入if判断语句
if not result:
    print("未成年")
else:
    print("成年")

# 用于声明无初始值内容的变量
name = None