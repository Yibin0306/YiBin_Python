"""
m，控制宽度，要求是数字，如果比数字本身宽度小，则不生效
.n，控制小数点精度，要求是数字，小于数字本身会四舍五入
m.n，控制宽度，控制精度
"""

class_name = "一班"
class_num = 52
class_age = 18.5
messages = "班级%s，班级人数为%5d，班级平均年龄为%.2f"%(class_name,class_num,class_age) # 按顺序占位
print(messages)