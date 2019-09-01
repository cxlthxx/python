# author:chenxl

# 打开文件第一个参数是路径，第二个参数是打开的模式
'''
"r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
"w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
"a"，以追加模式打开，写入到文件中的任何数据将自动添加到末尾
'''
import os
import sys

txt = open('test.txt','r')
for i in txt:
     print(i)
txt.close()
txt = open('test.txt','w')
txt.write('ni hoa ya \n ')
txt.writelines('ni ya ')
txt.close()

# 实际使用读取功能
with open('test.txt') as fobj:
    for line in fobj:
        print(line)

# 文本的统计工作
def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的相关信息

    :arg path: 要分析的文本文件的路径

    :return: 包含空格数、制表符数、行数的元组
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # 现在关闭打开的文件
    fd.close()

    # 以元组形式返回结果
    return spaces, tabs, i + 1

def main(path):
    """
    函数用于打印文件分析结果

    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False


if __name__ == '__main__':
    sys.argv.append('test.txt')
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

