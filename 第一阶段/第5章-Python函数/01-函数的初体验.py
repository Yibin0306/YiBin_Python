"""
函数：是组织好的，可重复使用的，用来实现特定功能的代码段
作用：为了针对一个特定需求、可供重复利于的代码段
     提高程序的重复性、减少重复性代码、提高开发效率
"""

# 列子
name = "cyb very cool"
length = len(name)
print(length)

"""
len()是python的内置函数：
是提前写好的，可以重复使用，实现统计长度
"""

# 列子
str1 = "cyb"
str2 = "very"
str3 = "cool"

num = 0
for i in str1 + str2 + str3:
    num += 1
print(num)

# 使用函数优化这个过程
def my_len (data):
    count = 0
    for f in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)