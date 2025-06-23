# 接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        print(f"读取全部的结果如下：\n{f.read()}")
    except Exception as e:
        print(f'程序有异常，原因是{e}')
    finally:
        if f:
            f.close() # 如果变量是None，表示False，如果有任何内容，表示True

# 收文件路径以及传入数据，将数据追加写入到文件中
def append_file_info(file_name, data):
    f = open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write('\n')
    f.close()