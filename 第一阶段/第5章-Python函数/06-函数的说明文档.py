# 函数的定义语法：
# def 函数名(传入参数):
#     """
#     函数说明
#     函数说明
#     ...
#     """
#     函数体
#     return 返回值

# 列
def add(x,y):
    """
    add函数可以接收两个参数，进行两数相加的功能
    :param x:形参x表示相加的第一个数字
    :param y:形参y表示相加的第二个数字
    :return:返回值是两数相加的结果
    """
    result = x + y
    print(f"两数相加的结果是：{result}")
    return result

add(5,6)
# 查看参考文档快捷键ctrl+q