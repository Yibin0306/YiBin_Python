# 导入自定义模块使用
import My_Package.my_module1
import My_Package.my_module2
My_Package.my_module1.func1(1, 2)
# 如果调用的两个模块中有相同的函数名称，后面的会覆盖前面的(这里没体现)
My_Package.my_module2.func1(3, 1)

"""
__main__变量
if __name__ == '__main__':
用于在模块里测试使用，不影响导入模块出来的结果

__all__变量，当使用from xxx import * 的时候，只导入__all__中的元素
"""
