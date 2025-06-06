"""
需求：
定义一个1-100的随机数字
1.无限次机会，直到猜中为止
2.每次猜不中，会提示大了或者小了
3.猜完数字后，提示猜了几次
"""
import random
num = random.randint(1, 100)
mark = True
frequency = 0
while mark:
    guess = int(input("请输入您猜测的数字:"))
    frequency += 1
    if guess == num:
        print("恭喜你答对了！")
        mark = False
    else:
        if guess > num:
            print("您猜测的数字大了")
        else:
            print("您猜测的数字小了")
print(f"您一共猜测了{frequency}次")