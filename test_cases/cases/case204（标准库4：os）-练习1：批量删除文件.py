# coding=gbk
import csv
import os  # 删除当前目录下的所有文件
import random
import yaml
import time
# def del_file(path):  # ../resources/csv
#     # 1、获取指定路径../resources/csv下的所有文件，返回值是一个列表
#     list = os.listdir(path)  # 用于返回指定的文件夹下包含的“文件或文件夹”
#     print(list)  # ['file2491.csv']
#     # 2、遍历获取到的列表
#     for i in list:
#         # 2.1、把遍历到的列表中的值（此处为文件名）与目录路径（../resources/csv/）进行拼接（../resources/csv/file2491.csv）
#         new_path = os.path.join(path, i)  # os.path.join：把目录和文件名合成一个路径（path：初始路径/i：初始路径文件夹下的“文件或文件夹”）
#         # 2.2、判断完整的路径（目录+文件）是否为目录
#         if os.path.isdir(new_path):  # 由于【../resources/csv/file2491.csv】不是目录（是目录＋文件）
#             # del_file(new_path)
#             print('此处是目录')
#         else:
#             os.remove(new_path)  # 删除指定路径的文件。如果指定的路径是一个目录，将抛出 OSError
#             print('执行删除指定的文件完成')
#
#
# del_file('../resources/csv')
'''
1、定义函数（可被调用）
'''
def writes():
    data = ["李白", "杜甫", "白居易", "王维"]
    if not os.path.exists('../../resources/csv/'):
        os.makedirs('../../resources/csv/')
    try:
        str_file = 'yaml' + str(random.randint(1000, 9999)) + '.csv'
        # print(str_file)
        with open('../resources/csv/' + str_file, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    finally:
        print('写入完成，要删除文件喽！')
        # os.remove('../resources/csv/' + str_file)

'''
2、执行删除文件夹操作
'''
def delete(path):
    # 2.1、新建要被删除的文件
    writes()
    # 2.2、删除文件夹下的所有文件
    lists = os.listdir(path)  # 用于返回指定的文件夹下包含的“文件或文件夹”

    for i in lists:
        new_paths = os.path.join(path, i)
        print('!!!!!!!' + str(new_paths))  # ../resources/csv\yaml2143.csv

        # os.path.isdir(path) 判断path是不是目录
        if os.path.isdir(new_paths):
            print('此处是目录')  # 由于../resources/csv/file2491.csv不是目录，则打印”此处是目录“（是目录＋文件）
        else:
            # os.remove(new_paths)
            print('已删除')

delete('../../resources/csv')

def test1():
    dit1={'name':'lilie ','age':12}
    if not os.path.exists('../../resources/yaml/'):
        os.makedirs('../../resources/yaml/')
    time1=time.time()
    print('time1:'+str(time1))
    timeArraw=time.localtime(time1)
    print('timeArraw:'+str(timeArraw))
    time_strf1=time.strftime('%Y-%m-%d %H:%M:%S',timeArraw)
    print('time_strf1:'+str(time_strf1))
    time_strf2=time.strftime('%Y-%m',timeArraw)
    print('time_strf2:'+str(time_strf2))
    time_strf3=time.strftime('%Y-%m-d %H:%M')
    print('time_strf3:'+str(time_strf3))
    time_strf4=time.strftime('%Y%m%d%H%M%S')

    str1=str(time_strf4)+str(random.randint(1000,9999))+'.yaml'
    print('str1:'+str1)
    try:
        with open('../../resources/yaml/' +str1, 'w', encoding='utf-8') as file1:
            file1.write(str(dit1))
    except IOError:
        print('报错')

    try:
        file1 = open('../../resources/yaml/' + str1, 'r', encoding='utf-8')
        data1 = yaml.load(file1, Loader=yaml.FullLoader)
        list1 = []
        list2 = []
        for k1, v1 in data1.items():
            list1.append(k1)
            list2.append(v1)
        print(list1)
        print(list2)
        dit2 = dict({list1[i]: list2[i] for i in range(len(list1))})
        print("dit2:"+str(dit2))
    finally:
        print('读取完成')
        file1.close()
    #   dict141 = dict({list2[i]: list3[i] for i in range(len(list3))})

    try:
        list_dit = os.listdir('../../resources/yaml/')
        for i in list_dit:
            path1 = os.path.join('../../resources/yaml/' + i)
            if os.path.isdir(path1):
                print('是目录')
            else:
                os.remove(path1)
    except PermissionError:
        print('权限报错')

def test2():
    dit2={'name':"lilei",'age':"19"}
    if not os.path.exists('../../resources/yaml/'):
        os.makedirs('../../resources/yaml')
    time2=time.time()
    time2_arrar=time.localtime(time2)
    time2_strf=time.strftime('%Y%m%d%H%M%S',time2_arrar)
    str2=str(time2_strf)+str(random.randint(100,999))+'.yaml'

    with open('../../resources/yaml/'+str2,'w',encoding='utf-*') as file2:
        file2.write(str(dit2))

    try:
        file2 = open('../../resources/yaml/' + str2, 'r', encoding='utf-8')
        data2 = yaml.load(file2, Loader=yaml.FullLoader)

        list3 = []
        list4 = []
        for k, v in data2.items():
            list3.append(k)
            list4.append(v)

        dit2 = dict({list3[i]: list4[i] for i in range(len(list3))})

        list5 = []
        for k, v in dit2.items():
            list5.append(k)
            list5.append(v)
    finally:
        file2.close()

    list_dir2=os.listdir('../../resources/yaml/')
    for i in list_dir2:
        path2=os.path.join('../../resources/yaml/', i)
        if os.path.isdir(path2):
            print('是目录')
        else:
            os.remove(path2)

def test3():
    dit3 = {'name': 'lilie', '性别': 'male'}
    if not os.path.exists('../../resources/yaml/'):
        os.makedirs('../../resources/yaml')
    time3 = time.time()
    time3_array = time.localtime(time3)
    time3_strf = time.strftime('%Y%m%d%H%M%S', time3_array)
    str3 = str(time3_strf) + str(random.randint(100, 999)) + '.yaml'

    with open('../../resources/yaml/' + str3, 'w', encoding='utf-8') as file3:
        file3.write(str(dit3))

    try:
        file3 = open('../../resources/yaml/' + str3, 'r', encoding='utf-8')
        data3 = yaml.load(file3, Loader=yaml.FullLoader)

        list5 = []
        list6 = []
        for k, v in data3.items():
            list5.append(k)
            list6.append(v)

        dit3 = dict({list5[i]: list6[i] for i in range(len(list5))})

        list5 = []
        for k, v in dit3.items():
            list5.append(k)
            list5.append(v)
    finally:
        file3.close()

    list_dir3 = os.listdir('../../resources/yaml/')
    for i in list_dir3:
        path3 = os.path.join('../../resources/yaml/', i)
        if os.path.isdir(path3):
            print('是目录')
        else:
            os.remove(path3)