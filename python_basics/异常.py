# author:chenxl

'''
访问一个未定义的变量则会发生 NameError。
TypeError 也是一种经常出现的异常。当操作或函数应用于不适当类型的对象时引发，一个常见的例子是对整数和字符串做加法。
使用 try...except 块来处理任意异常
使用 raise 语句抛出一个异常。
'''

try:
    raise ValueError("A value error happened.")
except ValueError:
    print("ValueError in our code.")
else:
    print('无异常发生')
finally:
    print('完成操作')

def Hours(minute):
    # 如果为负数则 raise 异常
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))

while True:
    # 函数调用及异常处理逻辑
    try:
        Hours(int(input('请输入时间：')))
    except:
        print("Parameter Error")