# author:chenxl
import sys
from collections import Counter

# class MyClass(object):
#     i = 12345
#     def f(self):
#         return 'hello world'
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = MyClass(3,4)
# print(x.r,x.i)
#

# 类的继承  一个类可以继承多个类
class Person(object):
    def __init__(self,name):
        self.name = name
    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grade(self):
        return 0

class Student(Person):
    def __init__(self,name,branch,year,grade):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
        self.grade = grade
    def get_details(self):
        return '{} studies {} and is in {} year.'.format(self.name,self.branch,self.year)
    def get_grade(self):
        common = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        print("Pass: {}, Fail: {}".format(n1, n2))


class Teacher(Person):
    def __init__(self,name,papers,grade):
        Person.__init__(self,name)
        self.papers = papers
        self.grade = grade
    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))
    def get_grade(self):
        s = []
        common = Counter(self.grade).most_common(4)
        for i, j in common:
            s.append("{}: {}".format(i, j))
        print(', '.join(s))

# person1 = Person('Sachin')
# student1 = Student('Kushal', 'CSE', 2005)
# teacher1 = Teacher('Prashad', ['C', 'C++'])
#
# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())

# 属性读取方法
# print(student1.branch)

person1 = Person('Sachin')
if sys.argv[1] == "student":
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()

class Student(Person):
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
    def get_details(self):
        return '{} studies {} and is in {} year.'.format(self.name,self.branch,self.year)

class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers
    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())

# 属性读取方法
print(student1.branch)

# 装饰器
class Account(object):
    def __init__(self,rate):
        self._amt = 0
        self.rate = rate
    @property
    def amount(self):
        """账号余额（美元）"""
        return  self._amt
    @property
    def cny(self):
        """账号余额（人民币）"""
        return self._amt * self.rate
    @amount.setter
    def amount(self,value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self._amt = value
if __name__ == '__main__':
    acc = Account(rate=6.6)  # 基于课程编写时的汇率
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -100
    print("Dollar amount:", acc.amount)
