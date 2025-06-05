"""
字符串格式化的语法
"%占位符"%变量
%表示：我要占位
s表示：将变量变成字符串放入占位的地方（将其它类型转换为字符串进行拼接）
"""

name = "深度学习"
messages = "我要学%s"%name
print(messages)

# 通过占位方式，完成数字和字符串的拼接
class_num = 52
class_age = 18
messages = "班级人数为%s，班级平均年龄为%s"%(class_num,class_age) # 按顺序占位
print(messages)

""""
常用的三类数据类型占位
%s表示：将变量变成字符串放入占位的地方
%d表示：将变量变成整数放入占位的地方
%f表示：将变量变成浮点数放入占位的地方
"""

class_name = "一班"
class_num = 52
class_age = 18.5
messages = "班级%s，班级人数为%d，班级平均年龄为%f"%(class_name,class_num,class_age) # 按顺序占位
print(messages)