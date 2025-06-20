"""
w模式
文件写入
f.write(" ")
内容刷新
f.flush()

注意：
    直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
    当调用flush或close的时候，内容会真正写入文件
    这样做是避免频繁的操作硬盘，导致效率下降
"""

f = open("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt","w",encoding="utf-8")
f.write("hello world\nhello world") # 将内容写道内存中
f.flush() # 将内存中积攒的内容写道硬盘文件当中
f.close() # close内置了flush的功能

# 写操作，如果文件不存在会创建文件，如果文件存在原本内容全部清空，在进行写入