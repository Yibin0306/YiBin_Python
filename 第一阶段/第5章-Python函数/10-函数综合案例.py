# 定义全局变量
name = input("请输入您的名字:")
money = 5000000
# 查询余额函数
def balance(show_header):
    if show_header:
        print("-----------------查询余额-----------------")
    print(f"{name}，您好，您的余额为:{money}元。")
# 存款函数
def deposit(add):
    global money
    money += add
    print("-----------------存款-----------------")
    print(f"{name}，您好，您存款:{add}元成功。")
    balance(False)
# 取款函数
def withdraw(sub):
    global money
    money -= sub
    print("-----------------取款-----------------")
    print(f"{name}，您好，您取款:{sub}元成功。")
    balance(False)
# 主菜单函数
def main():
    print("-----------------主菜单-----------------")
    print(f"{name}，您好，欢迎来到银行ATM系统。请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择:"))
# 调用函数
while True:
    keyboard = main()
    if keyboard == 1:
        balance(True)
        continue #可以不写，但是保持严谨
    elif keyboard == 2:
        deposit_a = int(input("请输入您的存款的金额:"))
        deposit(deposit_a)
        continue
    elif keyboard == 3:
        withdraw_a = int(input("请输入您的取款的金额:"))
        withdraw(withdraw_a)
        continue
    else:
        print("退出系统")
        break