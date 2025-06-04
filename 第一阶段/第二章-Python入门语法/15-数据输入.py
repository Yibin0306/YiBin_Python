"""
input语句
数据输出：print
数据输入：input
input获得键盘的输入内容
input(提示信息)
"""

# 法一
print("who are you?")
name = input()
print("oh yeah! you are " + name)

# 法二
name = input("who are you?")
print("oh yeah! you are " + name)

# 输入数字类型
num = input("你的手机密码是：")
print("你的手机密码类型是:",type(num))
# input默认为字符串类型