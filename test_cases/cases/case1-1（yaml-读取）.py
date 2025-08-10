import json

import pytest
import yaml

'''
1、分次读取 .yaml文件中的数据，每次读取的值单独执行一次脚本（读取几个数据，就运行几次脚本）
2、读取 .yaml函数后，要使用 .values()函数
3、读取的yaml文件中若包含中文，使用encoding='utf-8'会报错
4、读取的yaml文件中的数据不能换行，否则报错
'''


def load1(path):
    try:
        file = open(path, 'r', encoding='utf-8')
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    except UnicodeDecodeError:
        print("解码错误，尝试使用其他编码")


# {'data1': {'from_station': 'bj','to_station': 'hz'},'data2': {'from_station': 'sh','to_station': 'sz'},'data3': {'from_station': 'hf','to_station': 'nj'}}
@pytest.mark.parametrize('datas', load1('../../resources/yaml/station.yaml').values())
def test1(datas):
    '''
    第1次读取：{'from_station': 'bj', 'to_station': 'hz'}
    第2次读取：{'from_station': 'sh', 'to_station': 'sz'}
    第3次读取：{'from_station': 'hf', 'to_station': 'nj'}
    '''
    names = json.dumps(datas['from_station'], ensure_ascii=False)  # ensure_ascii=False：解决中文乱码
    print(names)
