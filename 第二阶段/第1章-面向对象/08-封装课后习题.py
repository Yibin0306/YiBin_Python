class Phone:
    __is_5g_enable = False

    # 提供私有成员变量
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g通话")

    # 提供公开成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

# 创建对象
phone = Phone()
phone.call_by_5g()