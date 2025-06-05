# 变量是用来记录数据
"""
变量格式:
变量名称 = 变量的值
"""

# 定义一个变量用于记录钱包余额
money = 100
print("钱包还有:",money)

# 假设花费了十元，两种写法
money -= 10
money = money - 10
print("钱包还有:",money,"元")

# +-*/

# 练习
money_1 = 50
icecream = 10
coke = 5
print("当前钱包余额:",money_1,"元")
money_1 -= 10
print("购买了冰淇淋，花费:",icecream,"元")
money_1 -= 5
print("购买了可乐，花费:",coke,"元")
print("当前钱包余额:",money_1,"元")