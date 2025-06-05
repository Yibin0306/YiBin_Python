"""
布尔类型（bool）
布尔属于数字类型
True表示真
False表示假
True本质数字记作1，False数字记作0

布尔类型数据格式
变量名称 = 布尔类型字面量
"""

result = 10 > 8
print("10>8的结果是:",result,"，类型是:",type(result))

"""
比较运算符
== 判断是否相等，相等返回true不相等返回false
!= 判断是否不相等，不相等返回true相等返回false
> 判断大小，满足左大于右返回true，不满足返回false
< 判断大小，满足右大于左返回true，不满足返回false
>= 判断大小，满足左大于等于右返回true，不满足返回false
<= 判断大小，满足右大于等于左返回true，不满足返回false
"""

result = "cyb" == "xjl"
print("两边是否相等:",result)