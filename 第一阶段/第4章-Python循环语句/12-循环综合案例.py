"""
自写
import random
money = 10000
for i in range(1,21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，绩效不满足，不给予工资")
    else:
        if money <= 0:
            print("工资发完了，下个月再领吧")
            break
        money -= 1000
        print(f"员工{i}发放工资1000元，账户余额还剩{money}元")
"""

# 教程写，个人感觉有bug，如果工余额0了并且下一名员工绩效不足还会继续判断，理应工资为0时立马结束循环，如上述代码
money = 10000
for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，绩效不满足，不给予工资")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}发放工资1000元，账户余额还剩{money}元")
    else:
        print("工资发完了，下个月再领吧")
        break