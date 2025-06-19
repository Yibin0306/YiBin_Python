"""
大概分为三步：打开文件、读写文件、关闭文件

一、 open函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下
    open(name,mode,encoding)
    name：是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
    mode：设计打开文件的访问模式（只读r，只写w，追加a等）
    encoding：编码格式（推荐使用UTF-8）

二、 read()方法
    文件对象.read(num)
    num表示要从文件中读取的数据长度（单位是字节），如果没有传入num，那么表示读取文件中所有的数据

    redLines()方法
    redLines()可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

    redLine()方法：一次读取一行内容
    for循环读取文件行

三、 close()关闭文件对象
    最后通过close，关闭文件对象，也就是关闭对文件的占用
    如果不调用close，同时程序没有停止运行，文件会一直被python程序占用

四、 with open 语句
    通过在with open的语句块中对文件进行操作
    可以在操作完成后自动关闭close文件，避免忘记close方法
"""
# 打开文件
f = open("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt","r",encoding="utf-8")
print(type(f))

# 读取操作 - read
# print(f"读取十个字节的结果{f.read(13)}") # 会记录读到哪里
# print(f"读取全部的结果{f.read()}") # 接着上面继续读取
print("---------------------------------------------")

# 读取操作 - redLines
# lines = f.readlines() #读取文件的全部行，封装到列表中
# print(f"lines列表的类型是{type(lines)}")
# print(f"lines列表的内容是{lines}")

# 读取操作 - redLine
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"读取的第一行数据：{line1}")
print(f"读取的第二行数据：{line2}")
print(f"读取的第三行数据：{line3}")

# 读取操作 - for循环
for line in f: # 读取文件是按照行为单位
    print(f"每一行数据是:{line}")

# 关闭文件
f.close() # 解除文件的占用

# with open 语句
with open("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt","r",encoding="utf-8") as f:
    for line in f: print(line) # 操作完成后自动关闭close文件，避免忘记close方法