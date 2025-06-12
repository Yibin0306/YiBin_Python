"""
字典：实现用key取出value的操作
字典的定义，同样使用{}，不过存储的元素是一个个的：键值对
    字面量
    {key:value，key:value，key:value，key:value，....}
    定义变量
    变量名称 = {key:value，key:value，key:value，key:value，....}
    定义空列表
    变量名称 = {}
    变量名称 = dict()

字典和集合一样，不可以用下标索引
字典的key和value可以是任意数据类型(key不可以是字典)

一、 从字典中基于key获得value
    语法：字典[key]
    结果：得到新的结果

二、 字典嵌套
    语法:{
        key:{
            key:value
        }
    }
"""

# 定义字典
my_dict = {"cyb":99,"xjl":88,"wgk":77}
my_dict_2 = {}
print(f"my_dict的内容是：{my_dict}，类型是：{type(my_dict)}")

# 定义重复key的字典
my_dict = {"cyb":99,"cyb":88,"wgk":77}
print(f"重复key的字典内容是：{my_dict}")# 字典中不支持重复的key

# 从字典中基于key获得value
my_dict = {"cyb":99,"xjl":88,"wgk":77}
score = my_dict["cyb"]
print(f"cyb的考试成绩是{score}")

# 定义一个嵌套字典
stu_score_dict = {
    "楚伊斌":{
        "语文":99,
        "数学":100,
        "英语":95
    },"徐嘉乐":{
        "语文":100,
        "数学":95,
        "英语":90
    },"王高科":{
        "语文":95,
        "数学":100,
        "英语":95
    }
}
print(f"学生的考试信息是：{stu_score_dict}")
# 从嵌套的字典中获得数据
print(stu_score_dict["楚伊斌"]["语文"])