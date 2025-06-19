"""
一、 位置参数：调用函数时根据函数定义的参数位置来传递参数
    def user_name(name,age,gender):
        print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
    user_name('cyb',18,'man')
    注意：传递的参数和定义的参数的顺序及个数必须一致

二、 关键字参数：函数调用时通过'键=值'形式传递参数
    作用：可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
    注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序

三、 缺省参数：缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
    注意：所有位置参数必须出现在默认参数前，包括函数定义和调用（默认值只能在最后）
    作用：当调用函数时没有传递参数，就会使用默认是用缺省参数对应的值
    注意：函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值

四、 不定长参数：不定长参数也可叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
    作用：当调用函数时不确定参数个数时，可以使用不定长参数
    不定长参数类型：
    1.位置传递
    注意：传进的所有参数都会呗args变量收集，他会根据传进的参数的位置合并成一个元组，args是元组类型
    2.关键字传递
    注意：参数是'键=值'形式的清空下，所有'键=值'都会呗kwargs接收，同时会根据'键=值'组成字典
"""

# 位置参数
def user_name(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_name('cyb',18,'man')

# 关键字参数
def user_info(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
# 函数调用时，如果有位置参数时，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序
user_info('xjl',gender='woman',age=20)

# 缺省参数
def user_info(name,age,gender='man'):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_info('xjl',age=20)
user_info('xjl',age=20,gender='woman')

# 不定长 - 位置不定长，*号
def user_info(*args):
    print(args)
user_info('tom')
user_info('tom',20)

# 不定长 - 关键字不定长，**号
def user_info(**kwargs):
    print(kwargs)
user_info(name='tom',age=20,gender='man')