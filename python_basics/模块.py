# author:chenxl
import os
import requests

import bars

bars.hashbar(10)

def view_dir(path='C:/Users/Administrator/Desktop/python/python_basics'):
    """
    这个函数打印给定目录中的所有文件和目录
    :args path: 指定目录，默认为当前目录
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end =' ')
    print()
view_dir()

def download(url):
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = 'test.txt'
    with open(filename,'w',encoding='utf-8') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")
if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)

#Tab 补全


