# 受传入字符串，将字符串反转返回
def str_reverse(s):
    """
    功能是将字符串反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

# 下标x和y，对字符串进行切片
def substr(s,x,y):
    """
    将指定的字符串进行切片
    """
    return s[x:y]