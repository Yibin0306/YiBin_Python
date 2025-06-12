"""
集合特点：不支持元素重复（自带去重功能）、并且内容无序
基础语法：
    字面量
    {元素，元素，元素，元素，....}
    定义变量
    变量名称 = {元素，元素，元素，元素，....}
    定义空列表
    变量名称 = set()

集合是无序的，所以集合不支持下标索引访问
一、 添加新元素
    语法：集合.add(元素)。将指定的元素，添加到集合内
    结果：集合本身被修改，添加了新元素

二、 移除元素
    语法：集合.remove(元素)，将指定元素从集合中移除
    结果：集合本身被修改，移除了元素

三、 随机取出一个元素
    语法：集合.pop()，功能，从集合中随机取出一个元素
    结果：会得到一个元素的结果。同时集合本身会被修改，元素会被移除

四、 清空集合
    语法：集合.clear()

五、 取2个集合的差集
    语法：集合1.different(集合2)，功能：取出集合1和集合2的差集(集合1有而集合2没有的)
    结果：得到一个集合，集合1和集合2不变

六、 消除2个集合的差集
    语法：集合1.different_update(集合2)，功能：对比集合1和集合2，在集合1内删除和集合2相同的元素
    结果：集合1被删除，集合2不变

七、 2个集合合并为1个
    语法：集合1.union(集合2)，功能：将集合1和集合2组成新的集合
    结果：得到新的集合，集合1和集合2不变

八、 统计集合元素数量
    语法：len(集合)

九、 集合的遍历（集合不支持下标索引，不支持while循环）可以用for循环
"""

# 定义集合
my_set = {"我","是","大帅哥","我","是","大帅哥"}
my_set_empty = set()
print(f"my_set的内容是: {my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是: {my_set_empty}，类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("handsome")
print(f"add_set添加元素后结果是: {my_set}")

# 移除元素
my_set.remove("是")
print(f"add_set移除元素后结果是: {my_set}")

# 随机取出一个元素
pop_set = my_set.pop()
print(f"add_set取出元素后结果是: {my_set}，集合被取出的元素是：{pop_set}")

# 清空集合
my_set.clear()
print(f"add_set被清空后结果是: {my_set}")

# 取2个集合的差集
new_set_1 = {1,2,3,4,5,6,7,8,9,10}
new_set_2 = {5,6,7,8}
different_set = new_set_1.difference(new_set_2)
print(f"different_set取2个集合的差集: {different_set}")

# 消除2个集合的差集
new_set_1 = {1,2,3,4,5,6,7,8,9,10}
new_set_2 = {5,6,7,8}
new_set_1.difference_update(new_set_2)
print(f"new_set_1集合的结果: {new_set_1}")
print(f"new_set_2集合的结果: {new_set_2}")

# 2个集合合并为1个
new_set_1 = {1,2,3,4,5,6,7,8,9,10}
new_set_2 = {5,6,7,8}
ner_set_3 = new_set_1.union(new_set_2)
print(f"new_set_3集合的结果: {ner_set_3}")# 集合有去重功能

# 统计集合元素数量
new_set_1 = {1,2,3,4,5,6,7,8,9,10}
len_set_1 = len(new_set_1)
print(f"new_set_1的元素有: {len_set_1}个")

# 集合的遍历
new_set_1 = {1,2,3,4,5,6,7,8,9,10}
for item in new_set_1:
    print(item)