# author:chenxl

# 字符串的方法
# split（）
import math
from filecmp import cmp

a = 'Shi Yan Lou'
# 根据指定字符分割
print(a.split())
# 首字母大写
print(a.title())
# 是否为标题
print(a.istitle())
# 全部大写
print(a.upper())
# 是否为全部大写
print(a.isupper())
# 全部小写
print(a.lower())
# 是否全部为小写
print(a.islower())
# 大小写交换
print(a.swapcase())
# 是否全部为字母和数字
print(a.isalnum())
# 是否只有字母
print(a.isalpha())
# 是否只有数字
print(a.isdigit())
# join() 连接列表内的字符串
print('-'.join(a.split()))
# strip() 不指定参数默认剥离首位的空格和换行符
s = 'a bca\n'
print(s.strip('a'))
s = "www.foss.in"
# 删除在字符串左边出现的'c','w','s','d','.'字符
print(s.lstrip("w."))
s = "www.foss.in"
# 删除在字符串右边出现的'c','n','w','d','i','.'字符
print(s.rstrip("cnwdi."))

s = 'faulty for a reason'
print(s.find('for'))
print(s.startswith('fa'))
print(s.endswith('reason'))

# 局域或全局变量
a = 9
def change():
    a = 90
    print(a)
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)

a = 9
def change():
    global a
    print(a)
    a = 100
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)


# 函数
def func(a,b=5,c=10):
    print('a is {} and b is {} and c is {}'.format(a,b,c))

func(12,24)
func(12,c=24)
func(b=12, c = 24, a = -1)
# 强制关键字参数
def hello(*,name='user'):
    print('hello',name)
hello(name = 'lin')

# 文档字符串
def longest_sid(a,b):
    '''
     Function to find the length of the longest side of a right triangle.
    :param a: Side a of the triangle
    :param b: Side b of the triangle
    :return: Length of the longest side c as float
    '''
    return  math.sqrt(a*a+b*b)
if __name__ == '__main__':
    print(longest_sid.__doc__)
    print(longest_sid(3,3))

# map函数
lst = [1,2,3,4,5]
def square(num):
    return num*num
print(list(map(square,lst)))

# sorted()排序函数
L=[('b',2),('a',5),('c',3),('d',4)]
print(sorted(L, key=lambda x: x[1]))
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda x: x[2],reverse=True))

# zip() 元祖的打包
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
d = zip(a,b,c)
print(list(d))

# filter() 过滤数据
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))