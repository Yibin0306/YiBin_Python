"""
continue:中断本次循环，直接进入到下一次循环
continue:for循环和while循环，效果一致

break:直接结束循环
break:for循环和while循环，效果一致
"""

# 练习1
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")

# 练习2
# for i in range(1,3):
#     print("语句1")
#     for j in range(1, 3):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# 练习3
# for i in range(1,6):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")

# 练习4
for i in range(1,3):
    print("语句1")
    for j in range(1, 3):
        print("语句2")
        break
        print("语句3")
    print("语句4")