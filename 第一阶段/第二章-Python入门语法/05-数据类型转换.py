"""
常见转换语句
int(x)将x转换成一个整数
float(x)将x转换成一个浮点数
str(x)将x转换成一个字符串
转换带有结果同type(x)
"""

# 将数字类型转换成字符串
num_str = str(123)
print(type(num_str),num_str)

float_str = str(12.3)
print(type(float_str),float_str)

# 将字符串转数字
num = int("11")
print(type(num),num)

num_1 = float("12.3")
print(type(num_1),num_1)
# 不可转换 int("字符串")
# 想要将字符串转换为数字，必须要求字符串内容都是数字

# 整数转换为浮点数
num_2 = float(12)
print(type(num_2),num_2)

# 浮点数转换为整数，向左取整，会丢失精度
num_3 = int(12.6)
print(type(num_3),num_3)