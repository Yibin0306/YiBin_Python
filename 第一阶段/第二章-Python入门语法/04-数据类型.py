"""
如何验证数据的类型？
格式:
type(被查看类型的数据)
"""

# 使用print直接输入信息
print("使用print直接输入信息:",type("测试"),type(25),type(25.5))

# 使用变量存储type()的结果（返回值）
string_type = type("测试")
int_type = type(25)
float_type = type(33.3)
print("使用变量存储type()的结果（返回值）:",string_type,int_type,float_type)

# 可以查看变量存储的数据类型
name = "cyb"
name_type = type(name)
print("可以查看变量存储的数据类型:",name_type)

"变量无类型，查看的是变量内数据的类型"