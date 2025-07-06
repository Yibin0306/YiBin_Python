"""
继承分为单继承和多继承
继承表示：将父类那里继承（复制）来成员变量和成员方法（不含私有）

单继承语法：
class 子类名（父类名）
    类内容体

多继承语法:
class 子类名（父类1，父类2，...，父类N，）
    类内容体
多继承的注意事项：
多个父类中，如果有同名的成员，那么默认以继承顺序（从左往右）为优先级
即：先继承的保留，后继承的被覆盖

pass关键字:补全语法，表示空
"""

# 单继承
class Phone:
    IMEI = None # 序列号
    producer = 'XiaoMi' #厂商
    def call_by_4g(self):
        print('4G通话')

class Phone2025(Phone):
    face_id = '1001' # 面部识别方法
    def call_by_5g(self):
        print('2025年新功能：5G通话')

phone = Phone2025()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 多继承
class NFC:
    nfc_type = '第五代'
    producer = 'HuaWei'
    def read_card(self):
        print('nfc读卡')
    def write_card(self):
        print('nfc写卡')

class RemoteControl:
    rc_type = '红外遥控'
    def control(self):
        print('红外遥控开启')

class my_phone(Phone2025,NFC,RemoteControl):
    pass

my_phone = my_phone()
my_phone.call_by_4g()
my_phone.call_by_5g()
my_phone.read_card()
my_phone.write_card()
my_phone.control()