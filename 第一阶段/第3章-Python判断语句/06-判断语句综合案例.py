"""
需求：
定义一个1-10的随机数字，通过三次判断来猜出数字
1.数字随机产生，范围1-10
2.有三次机会猜测数字，通过三层嵌套判断实现
3.每次猜不中，会提示大了或者小了
"""
import random
num = random.randint(1,10)
test = int(input("请说出第一次猜测的数字:"))
if test == num:
    print("恭喜你第一次就猜对了")
else:
    if test > num:
        print(f"没猜对，比{test}小")
    else:
        print(f"没猜对，比{test}大")
    test = int(input("请说出第二次猜测的数字:"))
    if test == num:
        print("恭喜你第二次猜对了")
    else:
        if test > num:
            print(f"没猜对，比{test}小")
        else:
            print(f"没猜对，比{test}大")
        test = int(input("请说出第三次猜测的数字:"))
        if test == num:
            print("恭喜你三次猜对了")
        else:
            print(f"Sorry，你输了，真正的数字为{num}")