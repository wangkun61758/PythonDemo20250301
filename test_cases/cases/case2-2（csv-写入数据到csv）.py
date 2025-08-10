# coding=gbk
import csv
import random


def test20():
    list = ["李白", "杜甫", "白居易", "王维"]
    str1 = str(random.randint(1000, 9999)) + '.csv'
    with open('../../resources/csv/' + str1, 'w', encoding='utf-8') as file:
        data = csv.writer(file)
        data.writerow(list)
