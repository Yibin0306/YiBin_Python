"""
格式
while 条件1:
    条件1满足时，做的事情1
    条件1满足时，做的事情2
    条件1满足时，做的事情3
    ......

    while 条件2:
        条件2满足时，做的事情1
        条件2满足时，做的事情2
        条件2满足时，做的事情3
        ......
"""
# 表白100天，每一天都会送10朵玫瑰
day = 1
while day <= 100 :
    print(f"今天是表白的第{day}天")
    day += 1
    hua = 1
    while hua <= 10 :
        print(f"送给第{hua}只玫瑰花")
        hua += 1
    print("我喜欢你")

print(f"坚持到{day - 1}天，表白成功")