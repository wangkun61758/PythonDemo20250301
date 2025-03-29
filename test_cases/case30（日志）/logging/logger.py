import logging
import sys
import colorlog


# 设置loggin的属性（控制台可以设置日志颜色，文件中日志不能设置颜色）
def log():
    '''
    %Y 四位数的年份表示（000-9999） %m 月份（01-12） %d 月内中的一天（0-31）%H 24小时制小时数（0-23） %M 分钟数（00=59） %S 秒（00-59）%p 本地A.M.或P.M.的等价符
    '''
    # 1、日期格式设置
    date_format = '%Y/%m/%d %H:%M:%S %p'

    '''
    %(asctime)s 时间 %(threadName)s 线程 %(filename)s 文件名 [line:%(lineno)d] 行数 %(levelname)s 级别 %(message)s 消息
    '''

    # A.1、控制台格式
    console_fmt = '%(log_color)s%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'

    # A.2、控制台输出不同级别日志颜色设置
    color_config = {
        'DEBUG': 'cyan',  # 青色
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'purple',  # 紫色
    }

    # A.3、设置“控制台日志”的格式和颜色
    console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
    # A.4、实例化“流句柄对象”
    console_handler = logging.StreamHandler(sys.stdout)  # 流句柄
    # A.5、“流句柄对象”设置格式
    console_handler.setFormatter(console_formatter)

    # B.1、输出文件格式
    file_fmt = '%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
    # B.2、设置“输出日志”的格式
    file_formatter = logging.Formatter(fmt=file_fmt)
    # B.3、实例化“文件句柄对象”
    file_handler = logging.FileHandler('log8.text', mode='w', encoding='utf-8')  # mode='w'是覆盖之前的日志， mode='a'是接着打印日志
    # B.4、“文件句柄对象”设置格式
    file_handler.setFormatter(file_formatter)

    # 2、logging日志格式设置
    logging.basicConfig(
        format=console_fmt,  # 控制台格式
        datefmt=date_format,  # 日期格式
        level=logging.DEBUG,  # 从DEBUG开始打印
        handlers=[
            file_handler,
            console_handler
        ]
    )


log()
