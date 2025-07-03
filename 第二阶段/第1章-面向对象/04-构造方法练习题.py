class Student:

    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

for i in range (1,6):
    print(f"当前录入第{i}名学生信息，总共需要录入5位学生信息")
    student = Student(input("请输入学生姓名:"),input("请输入学生年龄:"),input("请输入学生地址:"))
    print(f"第{i}位学生录入完成，学生姓名:{student.name},学生年龄:{student.age},学生地址:{student.addr}")