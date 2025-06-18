"""
一、 新增元素
    语法：字典[Key] = value，结果：字典被修改，新增了元素

二、 更新元素
    语法：字典[Key] = value，结果：字典被修改，元素被更新
    注意：字典Key不可以重复，所以对已存在的Key执行上述操作，就是更新Value的值

三、 删除元素
    语法：字典.pop(Key)，结果：获得指定Key的value，同时字典被修改，指定Key的数据被删除

四、 清空元素
    语法：字典.clear()，结果：字典被修改，元素被清空

五、 获取全部的Key
    语法：字典.keys()，结果：得到字典中的全部Key

六、 遍历字典
    获得全部key，for循环字典key，字典[key]获得value

七、 统计字典内的元素数量
    len()函数

八、 字典特点：
    1.可容纳多个数据
    2.可容纳不同类型的数据
    3.每一份数据都是KeyValue键值对
    4.通过key获得value，key不可重复（重复会覆盖）
    5.不支持下标索引
    6.可以修改（新增或者删除更新元素等）
    7.支持for循环，不支持while循环
"""

# 定义元素
my_dict = {"cyb":99,"xjl":88,"wgk":77}

# 新增元素
my_dict["nry"] = 55
print(f"字典新增元素后{my_dict}")

# 更新元素
my_dict["nry"] = 33
print(f"字典更新元素后{my_dict}")

# 删除元素
score = my_dict.pop("nry")
print(f"字典被移除了一个元素后{my_dict}，被移除的元素数据是{score}")

# 清空元素
my_dict.clear()
print(f"字典元素被清空后{my_dict}")

# 获得全部的Key
my_dict = {"cyb":99,"xjl":88,"wgk":77}
keys = my_dict.keys()
print(f"字典的全部Key是：{keys}")

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"将字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")
# 方式2：直接对字典for循环，每次都是直接得到key
for value in my_dict:
    print(f"将字典的key是:{value}")
    print(f"字典的value是:{my_dict[value]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典中键值对的数量为：{num}")