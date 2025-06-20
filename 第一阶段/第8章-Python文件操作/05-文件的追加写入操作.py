"""
a模式:文件追加
f.write(" ")
内容刷新
f.flush()
"""

f = open("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt","a",encoding="utf-8")
f.write("\nhello 河电大\nhello 电子信息") # 将内容写道内存中
f.close() # close内置了flush的功能

# a操作，如果文件不存在会创建文件，如果文件存在会在原本内容后进行追加
