"""
自写，完美无bug
r = open("D:/ProgramLearn/YiBin_Python/第一阶段/第8章-Python文件操作/txt/test.txt","r",encoding="utf-8")
w = open("D:/ProgramLearn/YiBin_Python/第一阶段/第8章-Python文件操作/txt/test_w.txt","w",encoding="utf-8")
for line in r:
    line = line.strip()
    line = line.split("，")
    for word in line:
        if word == "正式":
            w.write(str(line))
            w.write("\n")
r.close()
w.close()
"""

# 教程写
r = open("D:/ProgramLearn/YiBin_Python/第一阶段/第8章-Python文件操作/txt/test.txt","r",encoding="utf-8")
w = open("D:/ProgramLearn/YiBin_Python/第一阶段/第8章-Python文件操作/txt/test_w.txt","w",encoding="utf-8")
for line in r:
    line = line.strip()
    if line.split("，")[4] == "测试":
        continue # 进入下一次循环
    w.write(line)
    w.write("\n")
r.close()
w.close()