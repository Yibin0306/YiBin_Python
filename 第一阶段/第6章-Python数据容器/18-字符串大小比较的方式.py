"""
字符串所用的所有字符
大小写英文单词
数字
特殊符号
都有对应的ASCII码表

每一个字符都能对上一个：数字的码值
从头到尾一位一位比较，其中一位大，后面就无需比较了
通过ASCII码表确定字符对应的码值数字来确定大小
"""

print(f"abd大于abc，结果{'abd' > 'abc'}")

print(f"ab大于a，结果{'ab' > 'a'}")

print(f"a大于A，结果{'a' > 'A'}")

print(f"key2大于key1，结果{'key2' > 'key1'}")