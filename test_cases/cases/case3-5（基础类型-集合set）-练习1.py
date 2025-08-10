#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/30 19:51
=================================================='''


def test1():
    set1 = set([1, 5, 1, 11, 25])
    print(set1)  # {1, 11, 5, 25}
    set2 = set([1, 5, 1, 11])
    set3 = set1.union(set2)
    print(set3)  # {1, 5, 25, 11}
    set3.pop()
    print(set3)  # {5, 25, 11}
    set3.remove(5)
    print(set3)  # {25, 11}
    set3.discard(11)
    print(set3)  # {25}

    # {1, 11, 5, 25} {1, 5, 1, 11}
    a = set1.intersection(set2)
    print(a)  # {1, 11, 5}
    b = set1.isdisjoint(set2)
    print(b)  # False
    set1.update(set2)
    print(set1)  # {1, 5, 25, 11}
    set1.difference(set2)
    print(set1)  # {1, 5, 25, 11}
    set1.difference_update(set2)
    print(set1)  # {25}
