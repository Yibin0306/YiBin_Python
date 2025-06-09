"""
列表list基本语法：
字面量
[元素1，元素2，元素3，元素4，....]

定义变量
变量名称 = [元素1，元素2，元素3，元素4，....]

定义空列表
变量名称 = [] 或 变量名称 = list()
"""

my_list = ["cyb", 2, 3.4,True]
print(my_list)
print(type(my_list))

# 列表支持嵌套
test_list = [[1,2,3,4,5], [6,7,8,9]]
print(test_list)
print(type(test_list))