"""
当程序遇到BUG，那么接下来有两种情况：
    1.整个程序因为一个BUG停止运行
    2.对BUG进行提醒，整个程序继续运行

捕获异常的作用：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段
基本语法：
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码

捕获指定异常：
try:
    可能发生错误的代码
except NameError as e:
    如果出现异常执行的代码

捕获多个异常：
try:
    可能发生错误的代码
except (NameError, AttributeError):
    如果出现异常执行的代码

捕获所有异常
try:
    可能发生错误的代码
except Exception as e:
    如果出现异常执行的代码

异常else
try:
    可能发生错误的代码
except Exception as e:
    如果出现异常执行的代码
else:
    没有异常时执行的代码

异常的finally，无论是否异常都要执行的代码，列如关闭软件
try:
    可能发生错误的代码
except Exception as e:
    如果出现异常执行的代码
else:
    没有异常时执行的代码
finally:
    f.close()
"""

# 基本捕获语法
try:
    f = open('test.txt','r',encoding='utf-8')
except:
    print('不存在这个文件')

# 捕获指定的异常
try:
    print(name)
except Exception as e:# e是个别名，它里面记录着异常的具体信息
    print('出现变量未定义的异常')
    # print(e)

# 捕获多个异常
try:
    print(name)
    1/0
except(Exception,ZeroDivisionError) as e:
    print('出现变量未定义 或者 除于0的异常')
    # print(e)

# 捕获所有异常
try:
    1/0
except Exception as e:
    print('出现异常了')
    print(e)

# 异常else
try:
    print("hello")
except Exception as e:
    print('出现异常了')
    print(e)
else:
    print('没有出现异常')

# 异常的finally
try:
    1/0
except Exception as e:
    print('出现异常了')
else:
    print('没有出现异常')
finally:
    print("我必须执行")