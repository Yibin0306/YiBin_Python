"""
语法1 range(num)
获得一个从0开始，到num结束的数字数列（不包含num本身）

语法2 range(num1, num2)
获得一个从num1开始，到num2结束的数字数列（不包含num本身）

语法3 range(num1, num2,step)
获得一个从num1开始，到num2结束的数字数列（不包含num本身）
数字之间的步长，以step为准（step默认为1）
"""

num = range(6)
for x in num:
    print(x, end=" ")
print()

num = range(2,6)
for x in num:
    print(x, end=" ")
print()

num = range(2,6,2)
for x in num:
    print(x, end=" ")
print()

for x in range(5):
    print("送玫瑰花")

# 练习求一个数中有多少个偶数
count = 0
for x in range(1,100):
    if x % 2 == 0 :
        count += 1
print(f"1到100(不含100本身)共有{count}个偶数")