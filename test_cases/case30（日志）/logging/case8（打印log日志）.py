import logging
import os
import yaml
from test_cases.case30设置loogging的属性.logging.logger import log

# A.1、首先调用log()方法，设置loogging的属性 （方法中设置了logging的一些自定义属性）
log()


# <RequestsCookieJar[<Cookie PHPSESSID=b2n58milhcv5bt9ng1sqna8j9u for gamma-vms.56.cool/>, <Cookie SERVERID=7349dbf5589746919266ccf2e3cd1162|1680398478|1680398478 for gamma-vms.56.cool/>, <Cookie ingress_user_id=1680398479.08.20538.276188|d8c6d8cb6c73f72f411c4a27f7a6674a for gamma-vms.56.cool/>]>
def get_cookie():
    # 1、实例化一个cookie返回值
    cookies = {'PHPSESSID': 'htvoegt7rgb27fadl6d22calic',
               'SERVERID': '7349dbf5589746919266ccf2e3cd1162|1680399216|1680399216',
               'ingress_user_id': '1680399217.479.24061.806845|d8c6d8cb6c73f72f411c4a27f7a6674a'}

    # 2、遍历cookie返回值
    result = []
    i = 0

    for key, value in cookies.items():
        str_cookie = '{}={}'.format(key, value)
        result.append(str_cookie)  # append() 方法用于在列表末尾添加新的对象
        i = i + 1
        print('第' + str(i) + '次遍历结束list的值为：' + str(result))  # ['PHPSESSID=htvoegt7rgb27fadl6d22calic']

    token = str(result)
    print('最终获取的list是：' + token)

    # 3、获取的token写入到新建的token.yaml文件
    if not os.path.exists('../../../resources/token'):
        os.makedirs('../../../resources/token')
    with open('../../../resources/token/token.yaml', "w", encoding="utf-8") as f:
        f.write(token)

    # 4、读取写入token.yaml文件的token
    file = open('../../../resources/token/token.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print('读取到的token：' + str(data[0]))  # 读取列表中指定位置的值

    # A.2、根据设置的loogging的属性（比如格式、颜色等），进行打印
    logging.debug('读取到的token：' + str(data[0]))

    logging.info('读取到的token：' + str(data[0]))
    logging.warning('读取到的token：' + str(data[0]))
    logging.error('读取到的token：' + str(data[0]))
    logging.critical('读取到的token：' + str(data[0]))


get_cookie()
