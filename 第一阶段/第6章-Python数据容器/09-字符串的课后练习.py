"""
给定一个字符串："itheima itcast boxuegu"
统计字符串内有多少个"it"字符
将字符串内的空格，全部替换为字符："|"
并按照"|"进行字符串分割，得到列表
"""
my_str = "itheima itcast boxuegu"
count_my_str = my_str.count("it")
print(f"字符串{my_str}中有：{count_my_str}个it字符")
replace_my_str = my_str.replace(" ","|")
print(f"字符串{my_str}，被替换空格后，结果:{replace_my_str}")
split_replace_my_str = replace_my_str.split("|")
print(f"字符串{replace_my_str}，按照|分隔后，得到:{split_replace_my_str}")