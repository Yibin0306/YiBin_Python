"""
文件相关的类定义
"""
import json

from data_define import Record

# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def data_read(self)->list[Record]:
        # 读到的文件数据，读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可
        pass

class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件路径

    # 复写（实现抽象方法）父类的方法
    def data_read(self)->list[Record]:

        f = open(self.path, 'r', encoding='utf-8')
        record_list: list[Record] = []

        for line in f.readlines():
            line = line.strip()     # 消除每一行的/n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def data_read(self)->list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        record_list: list[Record] = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/Resources/可视化案例数据/面向对象案例/2011年1月销售数据.txt")
    list1 = text_file_reader.data_read()
    for i in list1:
        print(i)

    json_file_reader = JsonFileReader("D:/Resources/可视化案例数据/面向对象案例/2011年2月销售数据JSON.txt")
    list2 = json_file_reader.data_read()
    for l in list2:
        print(l)