"""
Union类型可以定义联合类型注解
"""
from typing import Union

# 变量类型注解示例
my_list:list[Union[str,int]] = [1, 2, "str"]
my_dict:dict[str, Union[str,int]] = {'name':'cyb','age':18}

# 函数类型注解示例
def func(data: Union[int,str]) -> Union[int,str]:
    pass
func()