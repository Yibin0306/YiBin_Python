"""
python包
package包
从物理上看是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件可以用于包含多个模块文件
从逻辑上看，包的本质仍然是模块

包的作用：当模块文件越来越多，包可以帮助我们管理这些模块，包的作用就是包含多个模块，但包的本质依然是模块

注意：必须在__init__.py文件内添加__all__ = []，控制允许导入的模块列表
"""

# 三种写法
# import My_Package.my_module1
# import My_Package.my_module2

# from My_Package import my_module1
# from My_Package import my_module2

from My_Package.my_module1 import func3
from My_Package.my_module2 import func2
func2()
func3()

from My_Package import * # 在__init__.py文件定义了__all__ = []
my_module1.func3()