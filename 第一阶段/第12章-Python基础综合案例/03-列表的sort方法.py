"""
列表的sort方法
列表.sort(key=选择排序依据的函数,reverse=True|False)
参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
参数reverse，是否反转排序的结果，Ture表示降序，False表示升序
"""
my_list=[["a",33],["b",55],["c",11]]

# 定义排序方法
def choose_sort_key(element):
    return element[1] # 下标1
my_list.sort(key=choose_sort_key,reverse=True)
print(my_list)

# 匿名lambda形式
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)