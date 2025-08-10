import random
import string


def test1():
    str1='lilei hameimei wangwu zhagnsan lisi zhaoer'
    print(str1[1:9])
    count=str1.count(' ')
    list1=str1.split(' ',count)
    print(list1)

    print(str1[1:2:-2])
    print(str1[:])
    print(str1[::-1])
    str1.upper()
    str1.lower()
    if str1.isdigit():
        print('数字')
    elif str1.isalpha():
        print('字母')
    print(str1.endswith(' er',2,10))
    print(str1.startswith('li',0,len(str1)))
    str1.replace('h','H')
    print(str1)
    print(str1.find('h',0,len(str1)))

    phoneNum = '135' + ''.join(random.choice(string.digits) for _ in range(8))
    print(phoneNum)
