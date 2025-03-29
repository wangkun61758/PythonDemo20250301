#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/11 12:33
=================================================='''
'''
字母异位词分组
'''
class Solution1(object):
    '''
    【如果a3不在dict1中】：{'aet': ['eat']}
    【否则a3在dict1中】：{'aet': ['eat', 'tea']}
    【打印list1】:[['eat', 'tea']]
    [['eat', 'tea']]
    '''
    def groupAnagrams(self, list_datas):
        list1=[]
        dict1={}
        for i in list_datas:
            a1 = list(i)
            print(a1)#['e', 'a', 't']
            a2 = sorted(a1)
            print(a2)#['a', 'e', 't']
            a3 = ''.join(a2)
            print(a3)#aet
            if a3 not in dict1:
                dict1[a3] = [i]
                print('【如果a3不在dict1中】：'+str(dict1))#{'aet': ['eat']}
            else:
                dict1[a3].append(i)
                print('【否则a3在dict1中】：'+str(dict1))#{'aet': ['eat', 'tea']}
        for key in dict1:#{'aet': ['eat', 'tea']}
            list1.append(dict1[key])
            print('【打印list1】:'+str(list1))# [['eat', 'tea']]
        print(list1)
        return list1

sol1=Solution1()
list_datas1 = ["eat", "tea", "tan"]
# list_datas = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol1.groupAnagrams(list_datas1)

class Solution2(object):
    def groupAnagrams(self, list_datas):
        list1=[]
        dict1={}
        for i in list_datas:
            a1=list(i)
            a2=sorted(a1)
            a3=''.join(a2)
            if a3 not in dict1:
                dict1[a3]=[i]
            else:
                dict1[a3].append(i)

        for key in dict1:
            list1.append(dict1[key])
        print(list1)
sol2=Solution2()
list_datas2 = ["eat", "tea", "tan"]
# list_datas = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol1.groupAnagrams(list_datas2)
