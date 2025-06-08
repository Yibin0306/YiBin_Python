name = input("请输入您的名字:")
money = 5000000
# 查询余额函数
def balance():
    print("-----------------查询余额-----------------")
    print(f"{name}，您好，您的余额为:{money}元。")
# 存款函数
def deposit(add):
    global money
    money += add
    print("-----------------存款-----------------")
    print(f"{name}，您好，您存款:{add}元成功。")
    print(f"{name}，您好，您的余额为:{money}元。")
# 取款函数
def withdraw(sub):
    global money
    money -= sub
    print("-----------------取款-----------------")
    print(f"{name}，您好，您取款:{sub}元成功。")
    print(f"{name}，您好，您的余额为:{money}元。")
# 主菜单函数
def main():
    print("-----------------主菜单-----------------")
    print(f"{name}，您好，欢迎来到银行ATM系统。请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    operate = int(input("请输入您的选择:"))
    if operate == 1:
        balance()
        main()
    elif operate == 2:
        deposit_a = int(input("请输入您的存款的金额:"))
        deposit(deposit_a)
        main()
    elif operate == 3:
        withdraw_a = int(input("请输入您的取款的金额:"))
        withdraw(withdraw_a)
        main()
    elif operate == 4:
        main()
    else:
        main()
# 调用函数
main()