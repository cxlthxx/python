# author:chenxl
import math
'''
关键字
False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not
class               from                or
continue            global              pass
'''
# help("keywords")

# #从键盘读取输入
# number = int(input("Enter an interger:"))
# if number <= 100:
#     print("Your number is less than or equal to 100")
# else:
#     print('Your number is greater than 100')
# # eval 可以吧字符串与list，tuple，dict转换
# # list 的转换
# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# b = eval(a)
# print(b)
# print(type(b))
# # tuple的转换
# a = "{1: 'a', 2: 'b'}"
# b = eval(a)
# print(b)
# print(type(b))
# #dict的转换
# a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
# b = eval(a)
# print(b)
# print(type(b))
# ''' eval(expression[, globals[, locals]])
# expression ： 字符串
# globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# '''
# age = 18
# print(eval("{'name':'linux','age':age}",{"age":1822},locals()))
# # 危险系数高 输入代码会被执行 会被恶意植入危险代码
# eval(input('输入代码：'))
# # 计算投资不达目的誓不罢休 一般是不知道终点的
# amount = float(input("Enter amount: "))  # 输入数额
# inrate = float(input("Enter Interest rate: "))  # 输入利率
# period = int(input("Enter period: "))  # 输入期限
# value = 0
# year = 1
# while year <= period:
#     value = amount + (inrate * amount)
#     if year == period:
#         print("Year {} Rs. {:.2f}".format(year, value))
#     amount = value
#     year += 1
# #求N个数的平均值
# sum = 0
# count = 0
# print('please input 10 numbers:')
# for i in range(0,10):
#     number = float(input())
#     sum += number
#     count += 1
# average = sum / 10
# print('sum = {:.2f},average = {:.2f},count = {}'.format(sum,average,count))
#
# a,b = 45,'你好'
# print(b)
# #元祖封装（tuple packing） 元祖不可变
# data = ("shiyanlou", "China", "Python")
# #元祖拆装（tuple unpacking）
# name, country,language = data
# print(name)
#
# #解二元一次方程
# a =int(input('a = '))
# b =int(input('b = '))
# c =int(input('c = '))
# d = b ** 2 - 4 * a * c
# if d < 0:
#     print('ROOTS are imaginary')
# else:
#     root1 = (-b + math.sqrt(d)) / (2 * a)
#     root2 = (-b - math.sqrt(d)) / (2 * a)
#     print('root1 = {}'.format(root1))
#     print('root2 = {:.0f}'.format(root2))
# #计算圆的面积
# area = 2 * 2 * math.pi
# print('{:.10f}'.format(area))
# #斐波那契数列
# a,b = 0,1
# while b < 100:
#     print(b,end=',')
#     a,b = b,a +b
# print()
# #列表
# a = [ 1, 1, 342, 223, 'India', 'Fedora',1]
# print(a[0:-1])
# # append() 在列表的末尾增加元素
# a.append('Lin')
# print(a)
# #insert() 在列表指定的位置增加元素
# a.insert(2,'你好')
# print(a)
# #count(s)  返回列表元素s的数量
# print(a.count(1))
# #remove(s) 移除列表中从左往右指定的第一个s元素
# a.remove(1)
# print(a)
# #del() 删除指定位置的元素
# del a[1]
# print('删除了第一个元素 {}'.format(a))
# #reverse 反转整个列表
# a.reverse()
# print(a)
# print(a[::-1])
# print(a[2::-1])
# #extend()把列表所有的元素添加到另外的列表末尾不创建新的对象
# b = [1,2.3]
# a.extend(b)
# print(a)
# #创建新的对象
# c = [1,2,3]
# d = [4,5.6]
# e = d + c
# print(e)
# #sort()  排序默认升序
# e.sort()
# print(e)
#
# # 列表用作栈 （后进先出） pop() 没有参数时弹出最后位置的元素，设置参数时弹出参数的元素,单参数设置为0时(先进先出)
# a = [1, 2, 3, 4, 5, 6,7]
# print(a.pop(0))
# print(a)
#
# # 列表推导式
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)
#
# squares = list(map(lambda i: i**2,range(10)))
# print(squares)
#
# squares = [i**2 for i in range(10)]
# print(squares)
#
# squares =  [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]  #等同于下面这个列子
# squares = []
# for x in [1,2.3]:
#     for y in [3,1,4]:
#         if x != y:
#             squares.append((x,y))
# #推导式可进行嵌套
# a = [1, 2, 3]
# z = [x + 1 for x in [x ** 2 for x in a]]
# print(z)
# y = []
# w = []
# for x in a:
#     y.append(x**2)
# for x in y:
#     w.append(x+1)
# print(w)
#
# #元祖是不可变的，由数个逗号分割符组成的 tuple,创建一个元素的元祖值后面必须跟一个逗号
# a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'
# print(type(a))
#
# # 集合无序不重复的集
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('apple' in basket)
#
# a = set('abracadabra')
# b = set('alacazam')
# print(a,b)
# #a 有而b没有的字母
# c = a -b
# print(c)
# # 存在于a 或b 的字母
# c = a | b
# # a和 b都有的字母
# c = a & b
# #存在于a或者b但不同时存在的字母
# c = a ^ b
# # pop() 随机删除 并打印   add（）随机增加
# basket.pop()
# print(basket)
# basket.add('你好')
# print(basket)
#
# # 字典是无序的键值对
# data = {'kushal': 'Fedora', 'kart_': 'Debian', 'Jace': 'Mac'}
# #创建新键值对
# data['kushal'] = 'lin'
# data['kushal1'] = 'lin'
# print(data)
# # 删除关键字的键值
# del data['kushal1']
# print(data)
# # 使用in查询是否存在指定键
# print('kushal'  in data)
# # 遍历字典使用items（）
# for x,y in data.items():
#     print('{} uses {}'.format(x,y))
# # 遍历添加数据
# data = {}
# data.setdefault("names",[]).append('ruby')
# data.setdefault("names",[]).append('Python')
# data.setdefault("names",[]).append('c')
# print(data)
# print(data.get('foo',0))
# # 遍历列表
# for i,j in enumerate(['a','b','c']):
#     print(i,j)
# # zip（）同时遍历两个序列
# a = ['Pradeepto', 'Kushal']
# b = ['OpenSUSE', 'Fedora']
# for x,y in zip(a,b):
#     print('{} user {}'.format(x,y))
#
# n = int(input("Enter the number of students: "))
# data = {} # 用来存储数据的字典变量
# Subjects = ('Physics', 'Maths', 'History') # 所有科目
# for i in range(0, n):
#     name = input('Enter the name of the student {}: '.format(i + 1)) # 获得学生名称
#     marks = []
#     for x in Subjects:
#         marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科的分数
#     data[name] = marks
# for x, y in data.items():
#     total =  sum(y)
#     print("{}'s total marks {}".format(x, total))
#     if total < 120:
#         print(x, "failed :(")
#     else:
#         print(x, "passed :)")

# 方正
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)

