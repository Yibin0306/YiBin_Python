"""
三引号和多行注释写法一样，支持换行操作
若使用变量接收，就是字符串
不用变量接收，就是多行注释
"""
name = '你好' # 单引号定义法
print(type(name))

name = "你好" # 双引号定义法
print(type(name))

#三引号定义法
name = """
你好
深度学习
"""
print(type(name),name)

# 在字符串中包含双引号
name = '"深度学习"'
name = "'深度学习'"
# 使用转义字符\解除引号的效用
name = "\"深度学习\""
print(name)