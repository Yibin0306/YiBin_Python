"""
while循环语法
while 条件：
    条件满足时，做的事1
    条件满足时，做的事2
    条件满足时，做的事2
    ....
"""

# 练习
i = 0
while i < 10:
    print(i)
    i += 1

"""
while的条件为布尔类型，true表示继续循环，false表示结束循环
需要设置循环终止条件
"""

# 练习1-100相加
num = 0
i = 1
while i <= 100:
    num = num + i
    i += 1
    print(num)