# coding=gbk
import csv

'''
李白,杜甫,张飞,赵云
张飞,赵云,吕布,韩信
张三,李四,王二,麻子
'''


def test1():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:  # gbk' 解决读取的中文无法解析的问题
        csv_data = csv.reader(file)
        for row in csv_data:
            list.append(row)
    file.close()
