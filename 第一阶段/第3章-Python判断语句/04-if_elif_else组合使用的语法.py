"""
格式：
if 条件1:
    满足条件1要做的事
elif 条件2:
    满足条件2要做的事
else:
    不满足所有条件要做的事

判断是互斥并且有顺序的
若满足条件1忽略条件2，以此类推
"""

# 练习
age = int(input("请先输入一个数字:"))
test_1 = int(input("请输入第一次猜想的数字:"))
test_2 = int(input("不对，再猜一次:"))
test_3 = int(input("不对，再猜最后一次:"))
if test_1 == age:
    print("恭喜你，猜对啦！")
elif test_2 == age:
    print("恭喜你，猜对啦！")
elif test_3 == age:
    print("恭喜你，猜对啦！")
else:
    print(f"Sorry，全部猜错了，我想的是:{age}")