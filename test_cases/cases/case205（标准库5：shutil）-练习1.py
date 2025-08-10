#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/11 13:24
=================================================='''
import shutil


def test1():
    shutil.copy('../../resources/data/order.yaml', '../../resources/abc')  # 将源文件复制到目标文件，并返回目标文件的路径
    print(shutil.copy('../../resources/data/order.yaml',
                      '../../resources/abc'))  # 将源文件复制到目标文件，并返回目标文件的路径../resources/abc\order.yaml

    '''
    1、要移动的文件路径不存在会报错
    2、要复制到的目录下已经存在要复制的文件也会报错
    '''
    # print(shutil.move('../resources/data/order.yaml','../resources/abc'))#移动文件或目录,，并返回目标文件的路径../resources/abc\order1.yaml

    '''
    shutil.rmtree(path, ignore_errors=False, onerror=None)
    path：必须是要删除的目录的路径(不能是文件路径)
    '''
    shutil.rmtree('../../resources/data/', ignore_errors=False, onerror=None)
    '''
    shutil.make_archive(base_name,format,dir)
    base_name为源文件路径
    format为压缩格式，可以是"zip", "tar", "gztar","bztar", or "xztar"
    dir为压缩后的文件路径
    '''
    shutil.make_archive('../../resources/data/order.yaml', 'zip', '../../resources/data/')
