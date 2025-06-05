"""
快速格式化方式
语法:f"内容{变量}"
"""

class_name = "一班"
class_num = 52
class_age = 18.5
messages = f"班级{class_name}，班级人数为{class_num}，班级平均年龄为{class_age}"
print(messages)

# 不关心类型，也不关心精度控制，对精度没有要求时使用