"""
类型注解主要功能：
    帮助第三方IDE工具对代码类型进行推断，协助做代码提示
    帮助开发者自身对变量进行类型注释
支持：
    变量的类型注解
    函数（方法）形参列表和返回值的类型注解
类型注解的两种语法：
    变量：类型
    # type：类型
一般无法直接看出变量类型的时候会添加变量的类型注解
"""
import json
import random

# 基础数据类型注解
var_1:int = 10
var_2:str = "my name is handsome"
var_3:bool = True

# 类对象类型注解
class Student:
    pass
stu:Student = Student()

# 基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {'cyb':18}

# 容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool] = (1,'str',False)
my_dict:dict[str:int] = {'cyb':18}

# 在注释中进行类型注解
var_1 = random.randint(1,10) # type:int
var_2 = json.loads('{"name":"cyb"}') # type:dict[str,str]
def func():
    return 10
var_3 = func() # type:int

# 类型注解的限制，非强硬性
var_4:str = 123 # 不会报错