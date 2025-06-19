"""
首先，在遍历上：
    五类数据容器都支持for循环遍历
    列表元组字符串支持while循环，集合、字典不支持（无法下标索引）

通用很多功能方法
比如len（容器）、max（容器）统计最大、min（容器）统计最小

可以通用类型转换
list（容器）转列表、str（容器）转字符串、tuple（容器）转元组、set（容器）转集合
不可以转换为字典，因为键值对，反之字典可以转换为其它容器

通用排序功能
sorted（容器，[reverse=true]）
将给定的容器进行排序
排序的结果会变成列表对象
"""

my_list = [3,1,2.3]
my_tuple = (1,3,True)
my_str = "cyb very cool"
my_set = {"我","是","大帅哥","我","是","大帅哥"}
my_dict = {"cyb":99,"xjl":88,"wgk":77}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 元素最大值是：{max(my_list)}")
print(f"元组 元素最大值是：{max(my_tuple)}")
print(f"字符串 元素最大值是：{max(my_str)}")
print(f"集合 元素最大值是：{max(my_set)}")
print(f"字典 元素最大值是：{max(my_dict)}")

# min最小元素
print(f"列表 元素最小值是：{min(my_list)}")
print(f"元组 元素最小值是：{min(my_tuple)}")
print(f"字符串 元素最小值是：{min(my_str)}")
print(f"集合 元素最小值是：{min(my_set)}")
print(f"字典 元素最小值是：{min(my_dict)}")

# 类型转换：容器转列表
print(f"列表转列表{list(my_list)}")
print(f"元组转列表{list(my_tuple)}")
print(f"字符串转列表{list(my_str)}")
print(f"集合转列表{list(my_set)}")
print(f"字典转列表{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表转元组{tuple(my_list)}")
print(f"元组转元组{tuple(my_tuple)}")
print(f"字符串转元组{tuple(my_str)}")
print(f"集合转元组{tuple(my_set)}")
print(f"字典转元组{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表转字符串{str(my_list)}")
print(f"元组转字符串{str(my_tuple)}")
print(f"字符串转字符串{str(my_str)}")
print(f"集合转字符串{str(my_set)}")
print(f"字典转字符串{str(my_dict)}")

# 类型转换：容器转集合
print(f"列表转集合{set(my_list)}")
print(f"元组转集合{set(my_tuple)}")
print(f"字符串转集合{set(my_str)}")
print(f"集合转集合{set(my_set)}")
print(f"字典转集合{set(my_dict)}")

# 通用排序功能
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
# 反转
print(f"列表对象的反向排序结果：{sorted(my_list,reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple,reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str,reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set,reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict,reverse=True)}")