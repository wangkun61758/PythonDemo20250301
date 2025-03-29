#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:33
=================================================='''
'''
1、lambda x, y为定义函数（相当于def test(x,y)）
2、x * x * x * y为函数体
'''
result1 = lambda x, y: x * y
print(result1(5, 2))

result2=lambda x,y,z: x*y*z
print(result2(5, 2, 3))

result3=lambda x,y,z: x*y*z
print(result3(5, 2, 3))

result4=lambda x,y,z: x*y*z
print(result4(5, 2, 3))

result5=lambda x,y:x*y
print(result5(5, 2))

result6=lambda x,y:x+y
print(result6(5, 2))

result7=lambda x,y:x*y
print(result7(5, 2))
'''
练习：2025/3/20（7）
'''
result8=lambda x,y,z: x*y*z
print(result8(5, 2, 3))
result9=lambda x,y,z: x*y*z
print(result9(5, 2, 3))
result10=lambda x,y,z:x*y*z
print(result10(2,3,6))
result11=lambda x,y,z: x*y*z
print(result11(2,3,6))
result12=lambda x,y,z: x*y*z
print(result12(2,3,6))
result13=lambda x,y,z: x*y*z
print(result13(2,3,6))
result14=lambda x,y,z: x*y*z
print(result14(2,3,6))
result15=lambda x,y,z: x*y*z
print(result15(2,3,6))
result16=lambda x,y,z: x*y*z
print(result16(2,3,6))
result17=lambda x,y,z: x*y*z
print(result17(2,3,6))