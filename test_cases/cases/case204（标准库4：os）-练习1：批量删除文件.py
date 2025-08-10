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


