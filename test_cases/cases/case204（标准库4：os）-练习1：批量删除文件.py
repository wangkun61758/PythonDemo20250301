# coding=gbk
import csv
import os  # ɾ����ǰĿ¼�µ������ļ�
import random
import yaml
import time
# def del_file(path):  # ../resources/csv
#     # 1����ȡָ��·��../resources/csv�µ������ļ�������ֵ��һ���б�
#     list = os.listdir(path)  # ���ڷ���ָ�����ļ����°����ġ��ļ����ļ��С�
#     print(list)  # ['file2491.csv']
#     # 2��������ȡ�����б�
#     for i in list:
#         # 2.1���ѱ��������б��е�ֵ���˴�Ϊ�ļ�������Ŀ¼·����../resources/csv/������ƴ�ӣ�../resources/csv/file2491.csv��
#         new_path = os.path.join(path, i)  # os.path.join����Ŀ¼���ļ����ϳ�һ��·����path����ʼ·��/i����ʼ·���ļ����µġ��ļ����ļ��С���
#         # 2.2���ж�������·����Ŀ¼+�ļ����Ƿ�ΪĿ¼
#         if os.path.isdir(new_path):  # ���ڡ�../resources/csv/file2491.csv������Ŀ¼����Ŀ¼���ļ���
#             # del_file(new_path)
#             print('�˴���Ŀ¼')
#         else:
#             os.remove(new_path)  # ɾ��ָ��·�����ļ������ָ����·����һ��Ŀ¼�����׳� OSError
#             print('ִ��ɾ��ָ�����ļ����')
#
#
# del_file('../resources/csv')
'''
1�����庯�����ɱ����ã�
'''
def writes():
    data = ["���", "�Ÿ�", "�׾���", "��ά"]
    if not os.path.exists('../../resources/csv/'):
        os.makedirs('../../resources/csv/')
    try:
        str_file = 'yaml' + str(random.randint(1000, 9999)) + '.csv'
        # print(str_file)
        with open('../resources/csv/' + str_file, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    finally:
        print('д����ɣ�Ҫɾ���ļ�ඣ�')
        # os.remove('../resources/csv/' + str_file)

'''
2��ִ��ɾ���ļ��в���
'''
def delete(path):
    # 2.1���½�Ҫ��ɾ�����ļ�
    writes()
    # 2.2��ɾ���ļ����µ������ļ�
    lists = os.listdir(path)  # ���ڷ���ָ�����ļ����°����ġ��ļ����ļ��С�

    for i in lists:
        new_paths = os.path.join(path, i)
        print('!!!!!!!' + str(new_paths))  # ../resources/csv\yaml2143.csv

        # os.path.isdir(path) �ж�path�ǲ���Ŀ¼
        if os.path.isdir(new_paths):
            print('�˴���Ŀ¼')  # ����../resources/csv/file2491.csv����Ŀ¼�����ӡ���˴���Ŀ¼������Ŀ¼���ļ���
        else:
            # os.remove(new_paths)
            print('��ɾ��')

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
        print('����')

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
        print('��ȡ���')
        file1.close()
    #   dict141 = dict({list2[i]: list3[i] for i in range(len(list3))})

    try:
        list_dit = os.listdir('../../resources/yaml/')
        for i in list_dit:
            path1 = os.path.join('../../resources/yaml/' + i)
            if os.path.isdir(path1):
                print('��Ŀ¼')
            else:
                os.remove(path1)
    except PermissionError:
        print('Ȩ�ޱ���')

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
            print('��Ŀ¼')
        else:
            os.remove(path2)

def test3():
    dit3 = {'name': 'lilie', '�Ա�': 'male'}
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
            print('��Ŀ¼')
        else:
            os.remove(path3)