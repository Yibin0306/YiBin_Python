"""
json是轻量级的数据交互格式，可以按照json指定的格式去组织和封装数据
json本质是一个带有特殊格式的字符串
python语言使用json优势很大：因为json无非是一个单独的字典或一个内部的元素都是字典的列表

主要功能：json就是一种在各个编程语言中流通的数据格式，负责不同编程语言的数据传递和交互
"""
# 导入json模块
import json
# 准备符合格式json格式要求的python数据
data = [{"name":"楚伊斌","age":18},{"name":"xjl","age":20},]
# 通过json.dumps(data)方法把python数据转化为json数据
data = json.dumps(data,ensure_ascii=False) # 如果有中文，用ensure_ascii=False不会乱码，表示不使用ascii码转换
print(type(data))
print(data)
# 通过json.loads(data)方法把json数据转化为了python数据
data = json.loads(data)
print(type(data))
print(data)