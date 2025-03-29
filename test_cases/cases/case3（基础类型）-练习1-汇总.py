import os.path


class Test:
    '''
     1、字符串的基本操作
     str.split()方法切割字符串后的结果，要赋给新的变量，直接打印 “str”打印的并不是切割后的结果
     '''

    def test_case1(self):
        txt = "Google#Runoob#Taobao#Facebook"
        print('打印坐标1~6：' + txt[1:7])

        # 方式1（.split() 返回分割后的字符串列表）
        x = txt.split('#', 2)  # 切割后要赋予某个变量【用#进行切割，并且将切割2次后的值赋予新的变量】
        print(x)  # 打印新的变量#['Google', 'Runoob', 'Taobao#Facebook']

        y=txt.split('#',3)
        print(y)

        # 方式2（.split() 返回分割后的字符串列表）
        print(txt.split('#', 2))  # 切割后要赋予某个变量【用#进行切割，并且将切割2次】

        str = 'abcdefg'
        print(str[0:-1])  # 输出第一个到倒数第二个的所有字符（左闭右开，-1为最后一个数字的位置，由于是右开，所以截取不到最后一个数字）

        print(txt.split('#', 1))
        print(txt.split('#', 2))
        print(txt.split('#', 3))

    '''
    2、列表的基本操作
    list相比元组：可编辑
    list列表相比set集合：有序、参数可以重复，效率低
    '''

    def test_case2(self):
        list = [1, 5, 66, 13, '谷歌', '特斯拉']
        # 1、打印指定位置的值
        print(list[4])
        print(list[1:3])

        # 2、切片操作
        print('列表切片：' + str(list[1:3]))  # 获得的切片为1~2
        # 3、添加元素
        list.append('金戒指')
        print(list)

        # 5、循环打印
        for i in list:
            print(i)
        # 6、两个列表转成一个字典
        list1 = ['name', 'age', 'car']
        list2 = ['lilei', 29, 'jeep']
        dict = {list1[i]: list2[i] for i in range(len(list1))}
        print('!!!!!!!!!!!!!!!!!' + str(dict))  # {'name': 'lilei', 'age': 29, 'car': 'jeep'}

    '''
    3、字典的基本操作
    '''

    def test_case3(self, space=' '):
        dit = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        print(dit['Name'])

        # 遍历key值
        for i in dit:
            print(i, dit[i])  # i为遍历的某个键，dit[i]为遍历的某个键对应的值（第一次遍历：Name Runoob）

        # 遍历key值
        for key in dit.keys():
            print(key, dit[key])  # key为遍历的某个键，dit[key]为遍历的某个键对应的值（第一次遍历：Name Runoob）

        # 遍历value值
        for value in dit.values():
            print(value, space * 5, end='')  # 遍历到的值为：Runoob      7      First

        # 删除字典 key（键）所对应的值，返回被删除的值。
        site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
        print('\n' + '删除的元素为：' + site.pop('name', '没有返回值'))  # 删除的元素为：菜鸟教程
        print('删除元素后的字典为：' + str(site))  # 删除元素后的字典为：{'alexa': 10000, 'url': 'www.runoob.com'}

        # 删除字典内所有元素
        tinydict = {'Name': 'Zara', 'Age': 7}
        tinydict.clear()
        print(tinydict)

        '''
        遍历字典，返回列表（将字典转换成列表）
        '''
        dit2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        result = []
        for k, v in dit2.items():
            result.append(k)
            result.append(v)

        print(result)  # ['Name', 'Runoob', 'Age', 7, 'Class', 'First']

    '''
    4、元组的基本操作
      list列表是可变的动态序列，可以访问，并增加、删除和修改列表中的元素，支持切片操作
      tuple元组是不可变的序列（静态序列），可以访问、不可以增、删、改元组中的元素，同样支持切片操作
    '''

    def test_case4(self):
        tup1 = ('Google', 'Runoob', 1997, 2000)
        print(tup1[1])

        print('元组切片：' + str(tup1[:4]))  # 切片为0~3

    '''
    5、set集合（无序、且不重复，可进行遍历）
    list列表相比set集合：有序、参数可以重复，效率低
    '''

    def test_case5(self):
        sets = set(("Google", "Runoob", "Taobao"))
        sets.add('牛二')  # 参数只能是元素
        print(sets)  # {'Google', 'Runoob', '牛二', 'Taobao'}

        list = [1, 5, 66, 13, '谷歌', '特斯拉']
        sets.update(list)  # 参数可以是列表，元组，字典等
        print(str(sets))  # {1, 66, 'Google', 5, 13, '牛二', 'Runoob', '特斯拉', 'Taobao', '谷歌'}

        list = []
        for i in sets:
            print(i)
            list.append(i)
        print(list)  # [1, 66, '特斯拉', '牛二', 5, 13, '谷歌', 'Runoob', 'Taobao', 'Google']

    ####################################################################
    def test_case6(self):
        dit = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for i in dit:
            print(i, dit[i])

        dit2 = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for key in dit2.keys():
            print(key, dit2[key])

        dit3 = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for value in dit3.values():
            print(value)

        set = {12, 356, 3, 98, 678}
        list = []
        for i in set:
            list.append(i)
        print(list)

    def test_case7(self):
        dit4 = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        list = []
        for key, value in dit4.items():
            strs = '{}={}'.format(key, value)
            print(strs)
            list.append(strs)
        print(list)  # 类型是list

        tokens = str(list)
        print(tokens)  # 类型是str
        if not os.path.exists('../../resources/token'):
            os.makedirs('../../resources/token')
        with open('../../resources/token/token.yaml', 'w', encoding='utf-8') as f:
            f.write(tokens)

    def test8(self):
        list1 = [1, 5, 66, 13, '谷歌', '特斯拉']
        print(list1[1:4])
        print(list1[2])
        print(list1[1:6:2])
        print(list1[1:6:3])
        print(list1[2:])
        print(list1[2::2])

        list2 = [12, 2, 34, 6, 145, 35]
        print(max(list2))
        print(min(list2))
        list2.append(222)
        print(list2)
        print(list2.count(2))

        list3 = list(range(5))
        list2.extend(list3)
        print(list2)

    def test9(self):
        list1 = []
        dit4 = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for k, v in dit4.items():
            str = '{}={}'.format(k, v)
            print(str)
            list1.append(str)
            print(list1)

    def test10(self):
        dit4 = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for k, v in dit4.items():
            str = '{}={}'.format(k, v)
            print(str)
        for i in dit4:
            print(i)
        for i in dit4:
            print(i, dit4[i])
        print(dit4['name'])

    def test11(self):
        dit = {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for i in dit:
            print(i,dit[i])

    def test12(self):
        dit= {'name': 'lilei', 'age': 18, 'sex': 'man'}
        for i in dit:
            print(dit[i])

    def test13(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        set1=set(nums1)
        set2=set(nums2)
        sets=set1&set2
        print(sets)

    def test14(self):
        s = "abaccdeff"
        dits = dict()
        for i in s:
            print(i)



