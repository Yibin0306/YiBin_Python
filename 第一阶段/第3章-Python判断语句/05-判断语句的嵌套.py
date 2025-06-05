"""
格式：
if 条件1:
    满足条件1要做的事
    if 条件2:
        满足条件2要做的事
elif 条件:
    满足条件要做的事
else:
    不满足所有条件要做的事

"""

# 练习
print("欢迎来到儿童游乐园，儿童免费，成人收费")
high = int(input("请输入你的身高:"))
if high > 120:
    print("您身高超出限制，需要补票10元")
    print("但是如果VIP等级大于3可以免费游玩")

    age = int(input("请输入你的VIP等级:"))
    if age < 3:
        print("您的VIP等级不够，需要补票10元")
    else:
        print("您的VIP等级达标，可以免费游玩")
else:
    print("欢迎小朋友，免费游玩！")