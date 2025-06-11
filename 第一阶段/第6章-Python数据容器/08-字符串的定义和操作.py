"""
字符串也是数据容器的一员
同元组一样，字符串是一个：无法修改的数据容器。

一、 index方法
    查询特定字符串的下标
    功能：查找指定字符串的的下标，如果找不到，会报错ValueError
    语法：字符串.index(字符串)

二、 字符串的替换
    语法：字符串.replace(字符串1，字符串2)
    功能：将字符串内的全部：字符串1替换为字符串2
    注意：不是修改字符串本身，而是得到了一个新字符串

三、 字符串的分割
    语法：字符串.split(分隔符字符串)
    功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
    注意：字符串本身不变，而是得到了一个列表对象

四、 字符串的规整操作(去前后空格)
    语法：字符串.strip()
    字符串的规整操作(去前后指定字符串)
    语法：字符串.strip(字符串)
    注意：传入的是"12",其实就是:"1"和"2"都会移除，是按照单个字符

五、 统计字符串个数
    语法：字符串.count(字符串)
    统计字符串中总共多少字符串
    语法：len(字符串)

六、 字符串特点：
    1.只可以存储字符串
    2.长度任意(取决于内存大小)
    3.支持下标索引
    4.允许重复字符串存在
    5.不可以修改(增加或删除元素等)
    6.支持循环
"""
my_str = "cyb very cool"

# 通过下标索引取值
value = my_str[2]
value1 = my_str[-1]
print(f"my_str下标为2的字母为：{value}\nmy_str下标为-1的字母为：{value1}")

# index方法
num = my_str.index("very")
print(f"在字符串{my_str}中查找very的起始下标是：{num}")

# 字符串的替换
new_my_str = my_str.replace("cool","handsome")# 得到一个新字符串
print(f"旧str：{my_str}\n新str：{new_my_str}")

# 字符串的分割
split_my_str = my_str.split(" ")# 按照空格分隔
print(f"分隔后的字符串为：{split_my_str}，类型为{type(split_my_str)}")

# 字符串的规整操作
strip_my_str_1 = "  cyb very cool  "
strip_my_str_2 = "12cyb very cool21"
print(strip_my_str_1.strip())
print(strip_my_str_2.strip("12"))# 传入的是"12",其实就是:"1"和"2"都会移除，是按照单个字符

# 统计字符串中某字符串的出现次数
num = my_str.count("c")
print(num)

# 统计字符串的长度
num = len(my_str)
print(num)