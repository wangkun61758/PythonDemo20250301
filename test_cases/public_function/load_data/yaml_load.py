import yaml


# 新建函数读取yaml文件（yaml格式内容的数据读取）
def load(path):
    file = open(path, 'r', encoding='utf-8')  # 1、打开文件('r':以只读的方式打开文件，编码方式：'utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)  # 2、读取yaml文件中的数据
    return data


def load2(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def load3(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def load4(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def load5(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def load6(path):
    file = open(path, 'r', encoding='utf_8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def load7(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data

def load8(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load9(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load10(path):
    file =open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load11(path):
    file =open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load12(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load13(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def load14(path):
    file =open(path,'r',encoding='utf-8')
    data=yaml.load(file)
    return data

def test1():
    file = open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    return data


def test2():
    file = open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)


def test3():
    file = open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)

def test15():
    file=open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    print(data)
    return data

def test16():
    file=open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def test17():
    file =open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def test18():
    file=open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

def test19():
    file=open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data =yaml.load(file,Loader=yaml.FullLoader)
    return data

def test20():
    file=open('../../../resources/data/order.yaml', 'r', encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data
