"""
需求：
定义一个1-10的随机数字，通过三次判断来猜出数字
1.数字随机产生，范围1-10
2.有三次机会猜测数字，通过三层嵌套判断实现
3.每次猜不中，会提示大了或者小了
"""
import random
num = random.randint(1,10)
test_1 = int(input("请说出第一次猜测的数字:"))
if test_1 == num:
    print("恭喜你第一次就猜对了")
    if test_1 > num:
        print(f"没猜对，比{test_1}小")
    else:
        print(f"没猜对，比{test_1}大")

    test_2 = int(input("请说出第二次猜测的数字:"))
    if test_2 == num:
        print("恭喜你第二次猜对了")
        if test_2 > num:
            print(f"没猜对，比{test_2}小")
        else:
            print(f"没猜对，比{test_2}大")

    test_3 = int(input("请说出第三次猜测的数字:"))
    if test_3 == num:
        print("恭喜你第二次猜对了")
        if test_3 > num:
            print(f"没猜对，比{test_3}小")
        else:
            print(f"没猜对，比{test_3}大")
    else:
        print("Sorry，你输了")