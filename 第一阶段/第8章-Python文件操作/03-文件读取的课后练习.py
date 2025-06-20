"""
自写（有bug）
f = open("D:/word.txt","r",encoding="utf-8")
num = 0
for line in f:
    my_str = str(line)
    if my_str.index("itheima"):
        num += 1
print(num)
"""
# 教程写
# 直接使用count方法统计
f = open("D:/word.txt","r",encoding="utf-8")
# num = f.read().count("itheima")
# print(num)

# 一行一行读取
num = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            num += 1
print(num)
f.close()