"""
模块的作用：模块是一个python文件，里面有类，函数，变量等，我们可以拿过来用（可以认为模块就是一个工具包）

模块的导入方式：
[from 模块名] import [模块 | 类 | 变量 | 函数 | *][as 别名]

常用的组合形式如：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名

一、 import 模块名
    import 模块名1,模块名2
    模块名.功能名()

二、 from 模块名 import 功能名
    功能名()

三、 from 模块名 import *
    功能名()

四、 import 模块名 as 别名
    别名.功能名()
    from 模块名 import 功能名 as 别名
    别名()
"""
# import 模块名
import time
print("开始")
time.sleep(2) # 通过点使用全部功能（类，函数，变量）
print("结束")

# from 模块名 import 功能名
from time import sleep
sleep(2)

# from 模块名 import *
from time import *
print("开始")
sleep(2)
print("结束")