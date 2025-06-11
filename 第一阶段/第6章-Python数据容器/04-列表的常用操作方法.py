"""
一、 方法概念
    在python中，如果将函数定义为class(类)的成员，那么函数称为：方法
    函数的使用：num = add(1,2)
    方法的使用：student = Student()
              num = student.add(1,2)

二、 index方法
    查询某元素的下标
    功能：查找指定元素在列表的下标，如果找不到，会报错ValueError
    语法：列表.index(元素)

三、 修改特定位置的元素值：
    语法：列表[下标] = 值

四、 插入元素
    语法：列表.insert(下标,元素)。在指定的下标位置，插入指定的元素

五、 追加元素
    语法：列表.append(元素)。将指定元素，追加到列表的尾部
    追加元素方式二
    语法：列表.extend(其它数据容器)。将其它数据容器的内容取出，依次追加到列表尾部

六、 删除元素
    语法一：del列表[下标]
    语法二：列表.pop(下标)（可以当返回值去得到）
    删除某元素在列表的第一个匹配项
    语法：列表.remove(元素)。如果有相同元素从前往后从第一个元素

七、 清空元素
    语法：列表.clear()

八、 统计元素个数
    语法：列表.count(元素)
    统计列表总共多少元素
    语法：len(列表)

九、 列表特点：
    1.可容纳多个元素（上限为2**63-1）
    2.可容纳不同类型的元素（混装）
    3.数据是有序存放的（有下标序号）
    4.允许重复数据存在
    5.可以修改

"""

my_list = ["cyb",2,3,4,5]
add_list = ["追加","的容器"]
# 查找某元素在列表内的下标索引
learn_index = my_list.index(4)
print(learn_index)

# 修改特定位置的元素值
my_list[1] = "cyb very cool"
print(my_list)

# 插入元素
my_list.insert(2,"下标2被插入的元素")
print(my_list)

# 追加元素
my_list.append("追加的元素")
print(my_list)
# 追加元素方式二
my_list.extend(add_list)
print(my_list)

# 删除元素
del my_list[-1]
element = my_list.pop(-1)
print(my_list, f"删除的元素是：{element}")
# 删除某元素在列表的第一个匹配项
my_list.remove("下标2被插入的元素")
print(my_list)

# 清空元素
my_list.clear()
print(my_list)

# 统计元素个数
my_list = ["cyb",2,3,2,5]
print(my_list.count(2))
# 统计列表总共多少元素
num = len(my_list)
print(num)