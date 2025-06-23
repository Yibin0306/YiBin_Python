# 引入软件包
import my_utils.str_util as str_util
import my_utils.file_util as file_util

# 受传入字符串，将字符串反转返回
my_str = str_util.str_reverse("哥帅大，是我")
print(my_str)

# 下标x和y，对字符串进行切片
my_str = str_util.substr("0123456789",3,6)
print(my_str)

# 接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
file_util.print_file_info("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt")
file_util.print_file_info("C:/Users/YiBin/Desktop/test.txt")

# 收文件路径以及传入数据，将数据追加写入到文件中
file_util.append_file_info("C:/Users/YiBin/Desktop/Personal Data/本科毕业论文/论文资料/测试.txt","123")