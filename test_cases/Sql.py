#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/18 22:58
=================================================='''


def test1():
    '''
    SELECT *  FROM
 (SELECT *,DENSE_RANK() OVER (ORDER BY score DESC) as rank
     FROM students
     WHERE class_id = '你的班级ID') ranked_students  WHERE rank = 2
    '''

    '''
    delete‌：只删除表中的数据，保留表结构。
    truncate‌：删除表中所有数据，但不删除表结构。
    drop‌：删除表中的数据和表结构
    '''