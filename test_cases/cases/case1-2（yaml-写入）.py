import os.path
import yaml
import jsonpath

def write_data():
    dit = {'Order1': {'errmsg': '保存成功1', 'status': 200}, 'Order2': {'errmsg': '保存成功2', 'status': 200}}
    if not os.path.exists('../../resources/token'):
        os.makedirs('../../resources/token')
    with open('../../resources/token/dict.yaml', 'w', encoding='utf-8') as f:
        # 写入yaml的数据要为str类型
        f.write(str(dit))
write_data()
######################################################################
def test_write():
    dit = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list = []
    for key, value in dit.items():
        list.append(key)
        list.append(value)
    string = str(list)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dit/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(string)
    f = open('../../resources/dit/dict.yaml', 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)  # ['name', '韩梅梅', 'age', 19, 'car', 'jeep']
test_write()
def test1():
    dit = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k, v in dit.items():
        list1.append(k)
        list2.append(v)

    print(list1)
    print(list2)

    for i in range(len(list1)):
        dit1 = '{}:{}'.format(list1[i], list2[i])
        print(dit1)
def test2():
    dit = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k, v in dit.items():
        list1.append(k)
        list2.append(v)

    dit2 = {list1[i]: list2[i] for i in range(len(list1))}  # {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}

    print(dit2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dit2))

    list_file = os.listdir('../../resources/dict')
    for file in list_file:
        path = os.path.join('../../resources/dict', file)
        if os.path.isfile(path):
            print('文件')
            # os.remove(path)
        elif os.path.isdir(path):
            print('目录')
def test3():
    dit1 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k, v in dit1.items():
        list1.append(k)
        list2.append(v)
    dict2 = {list1[i]: list2[i] for i in range(len(list1))}
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
def test4():
    dict1={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
def test5():
    dict1={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
def test6():
    dict1={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1=[]
    list2=[]
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
def test7():
    dict1={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1=[]
    list2=[]
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
def test8():
    dict1 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    # dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    dict2 = {list1[i]: list2[i] for i in range(len(list1))}
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
'''
练习：2025/3/20（1）
'''
def test9():
    dict1 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2={list1[i]:list2[i] for i in range(len(list1))}
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict1.yaml', 'w', encoding='utf-8') as file:
        # file.write(str(dict2))
        file.write(str(dict2))
def test10():
    dict1={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    list1=[]
    list2=[]
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1)) })
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict1.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict2))
