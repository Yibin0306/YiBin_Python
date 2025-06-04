"""
算数运算符
+-*/加减乘除
//取整除
%取余
**指数
"""

# 算数运算符
print("1+1=",1+1)
print("2-1=",2-1)
print("2*3=",2*3)
print("2/3=",2/3)
print("4//3=",4//3)
print("4%3=",4%3)# 4除3余1
print("2**3=",2**3)

# 赋值运算符 =
num = 1+2*3
print(num)

"""
复合赋值运算符
+= 加法赋值运算符 c+=a 等效于 c=c+a
-= 减法赋值运算符 c-=a 等效于 c=c-a
*= 乘法赋值运算符 c*=a 等效于 c=c*a
/= 除法赋值运算符 c/=a 等效于 c=c/a
%= 取模赋值运算符 c%=a 等效于 c=c%a
**= 幂赋值运算符 c**=a 等效于 c=c**a
//= 取整赋值运算符 c//=a 等效于 c=c//a
"""

# 复合赋值运算符
num_1 = 1
num_1 += 1
print("num_1 += 1:",num_1)
num_1 -= 1
print("num_1 -= 1:",num_1)

num_1 = 2
num_1 /= 2
print("num_1 /= 2:",num_1)
num_1 = 2
num_1 *= 2
print("num_1 *= 2:",num_1)
num_1 = 3
num_1 %= 2
print("num_1 %= 2:",num_1)
num_1 = 2
num_1 **= 2
print("num_1 **= 2:",num_1)
num_1 = 9
num_1 //= 2
print("num_1 //= 2:",num_1)