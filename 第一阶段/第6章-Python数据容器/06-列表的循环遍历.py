"""
将容器内的元素依次取出进行处理的行为，称之为：遍历、迭代

列表遍历-while循环
index = 0
while index < len(列表):
    元素 = 列表[index]
    对元素进行处理
    index += 1

列表遍历-for循环
for 临时变量 in 数据容器:
    对临时变量进行处理

while循环和for循环，都是循环语句，但细节不同：
在循环控制上:
    while循环可以自定循环条件，并自行控制
    for循环不可以自定循环条件，只可以一个个从容器内取出数据
在无限循环上:
    while循环可以通过条件控制做到无限循环
    for循环理论上不可以，因为被遍历的容器容量不是无限的
在使用场景上:
    while循环适用于任何想要循环的场景
    for循环适用于，遍历数据容器的场景或简单的固定次数循环场景
"""

# 列表遍历-while循环
def list_while_func():
    my_list = [21,25,21,23,22,20]
    num = 0
    while num < len(my_list) :
        element = my_list[num]
        print(f"下标为{num}的列表的元素为：{element}")
        num += 1
list_while_func()

# 列表遍历-for循环
def list_for_func():
    my_list = [21, 25, 21, 23, 22, 20]
    # for element in range(len(my_list)):
    #     print(f"下标为{element}的列表的元素为：{my_list[element]}")
    for element in my_list:
         print(f"下标为{my_list.index(element)}的列表的元素为：{element}")
list_for_func()

"""
定义—个列表，内容是：[1,2,3,4,5,6,7,8,9,10]
    遍历列表，取出列表内的偶数，并存入一个新的列表对象中
    使用while循环和for循环各操作一次
"""
my_list = [1,2,3,4,5,6,7,8,9,10]
add_list_while = []
num = 0
while num < len(my_list):
    element = my_list[num]
    if element % 2 == 0:
        add_list_while.append(element)
    num += 1
print(f"通过while循环，从列表：{my_list}中取出偶数，组成新列表：{add_list_while}")

add_list_for = []
for element in my_list:
    if element % 2 == 0:
        add_list_for.append(element)
print(f"通过for循环，从列表：{my_list}中取出偶数，组成新列表：{add_list_for}")