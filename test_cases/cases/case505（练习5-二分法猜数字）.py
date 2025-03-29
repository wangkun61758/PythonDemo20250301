#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 22:04
=================================================='''
import random


# def test():
#     number = random.randint(1, 100)
#     print('随机生成的数字为：' + str(number))
#
#     while True:
#         guess = int(input("请猜一个0到100之间的整数："))
#         if guess == number:
#             print("恭喜你，猜对了！")
#             break
#         elif guess < number:
#             print("猜小了，请再试一次。")
#         else:
#             print("猜大了，请再试一次。")
#
#
# test()

# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binary(arr, l, r, x):  # ([2, 3, 4, 10, 40],0,4,10)
    # 基本判断
    if r >= l:
        mid = int(l + (r - l) / 2)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binary(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binary(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1

# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

# 函数调用
result = binary(arr, 0, len(arr) - 1, x)

if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")
