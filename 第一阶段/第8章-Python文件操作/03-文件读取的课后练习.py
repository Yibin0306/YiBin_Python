"""
自写
f = open("D:/word.txt","r",encoding="utf-8")
num = 0
for line in f:
    my_str = str(line)
    if my_str.index("itheima"):
        num += 1
print(num)
"""
# 教程写
f = open("D:/word.txt","r",encoding="utf-8")
num = f.read().count("itheima")
print(num)