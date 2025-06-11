"""
元组同列表一样，都是可以封装多个、不同类型的元素在内
但最大的不同在于：
    元组一旦定义完成，就不可以修改
适用场景：需要在程序内封装数据，但又不希望封装的数据被篡改

元组定义语法：
    字面量
    (元素1，元素2，元素3，元素4，....)
    定义变量
    变量名称 = (元素1，元素2，元素3，元素4，....)
    定义空列表
    变量名称 = () 或 变量名称 = tuple()

一、 index方法
    查询某元素的下标
    功能：查找指定元素在元组的下标，如果找不到，会报错ValueError
    语法：元组.index(元素)

二、 统计元素个数
    语法：元组.count(元素)
    统计元组总共多少元素
    语法：len(元组)
"""

# 定义元组
my_tuple = (1,"cyb",True)
my_tuple1 = ()
my_tuple2 = tuple()
print(f"my_tuple类型是: {type(my_tuple)}，内容是：{my_tuple}")
print(f"my_tuple1类型是: {type(my_tuple1)}，内容是：{my_tuple1}")
print(f"my_tuple2类型是: {type(my_tuple2)}，内容是：{my_tuple2}")

# 定义单个元素的元组
my_tuple3 = ("hello",) # 单个元素的元组后写上单独的逗号才是元组
print(type(my_tuple3))

# 元组的嵌套
my_tuple4 = ((1,2,3),(4,5,6))
print(f"my_tuple4类型是: {type(my_tuple4)}，内容是：{my_tuple4}")

# 下标索引去取出内容
t1 = my_tuple4[-1][-1]
print(f"t1类型是: {type(t1)}，内容是：{t1}")

# 查询某元素的下标
my_tuple5 = ("cyb",2,3,4,2)
num = my_tuple5.index(2)
print(f"在元组my_tuple5中查找2的下标是{num}")

# 统计元素个数
num1 = my_tuple5.count(2)
print(f"在元组my_tuple5中查找2的个数是{num1}")
num2 = len(my_tuple5)
print(f"元组my_tuple5中元素的个数是{num2}")

# while遍历元组
num3 = 0
while num3 < len(my_tuple5):
    element = my_tuple5[num3]
    print(f"下标为{num3}的列表的元素为：{element}")
    num3 += 1

# for遍历元组
for element in my_tuple5:
    print(f"下标为{my_tuple5.index(element)}的列表的元素为：{element}")

# tuple中嵌套list的情况下可以修改list内容
t = (1,9,[5,6])
t[-1][0] = 4
print(t)