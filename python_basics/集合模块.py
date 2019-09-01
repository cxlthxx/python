# author:chenxl

from collections import Counter
import re
from collections import defaultdict
from collections import namedtuple

# 正则匹配文档中小写单词的匹配个数
path = 'test.txt'
words = re.findall('\w+', open(path,encoding='utf-8').read().lower())
print(Counter(words).most_common(10))

#Counter 对象有一个叫做 elements() 的方法，其返回的序列中，依照计数重复元素相同次数，元素顺序是无序的。
c = Counter(a=4,b=2,c=0,d=-2)
print(c)
print(list(c.elements()))

# most_common() 方法返回最常见的元素及其计数，顺序为最常见到最少。
print(Counter('abracadabra').most_common(3))

# defaultdict 是内建 dict 类的子类，它覆写了一个方法并添加了一个可写的实例变量
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for  x,y in s:
    d[x].append(y)
print(d)
print(d.items())

# 命名元组有助于对元组每个位置赋予意义，并且让我们的代码有更好的可读性和自文档性。
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x+p.y)
print(p[1])
x,y = p
print(y)