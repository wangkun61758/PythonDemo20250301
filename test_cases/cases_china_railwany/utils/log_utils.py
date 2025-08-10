# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# '''=================================================
# @Author ：kw
# @IDE    ：PyCharm
# @Date   ：2025/4/3 23:18
# =================================================='''
# import logging
# from datetime import datetime
#
# '''
# DEBUG‌：详细调试信息，通常用于开发过程中。
# INFO‌：一般信息，用于记录程序运行状态。
# WARNING‌：警告信息，表示可能会出现问题的情况。
# ERROR‌：错误信息，表示程序运行中出现的错误。
# CRITICAL‌：严重错误，通常表示程序无法继续运行。
# %(asctime)s（时间戳）、
# %(levelname)s（日志级别）、
# %(name)s（日志记录器名称）、
# %(message)s（日志内容）
# '''
# def init_logger():
#     # 1、创建Logger对象（日志记录器对象）
#     logger = logging.getLogger("api_test")#创建指定名称的（api_test）日志记录器对象
#     logger.setLevel(logging.INFO)#设定日志记录器对象的最低级别一般信息
#
#     # 2.1、定义日志格式
#     formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")#定义日志消息的显示格式
#     # 2.2、创建控制台Handler对象
#     file_handler = logging.FileHandler(f"../reports/{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")#将日志记录输出到一个文件中
#     # 2.3为“控制台Handler对象”设置日志格式
#     file_handler.setFormatter(formatter)
#
#     #3、将“控制台Handler对象”添加到日志记录器对象“Logger对象”上
#     logger.addHandler(file_handler)
#     return logger
# logger = init_logger()
