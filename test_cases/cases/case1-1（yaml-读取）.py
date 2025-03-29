import json

import pytest
import yaml
from contourpy.util import data

from test_cases.public_function.load_data import yaml_load

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
    names = json.dumps(datas['from_station'], ensure_ascii=False)#ensure_ascii=False：解决中文乱码
    print(names)
@pytest.mark.parametrize('datas', load1('../../resources/yaml/station.yaml').keys())
def test2(datas):
    print(datas)  # data1
@pytest.mark.parametrize('datas', load1('../../resources/yaml/station.yaml'))
def test3(datas):
    print(datas)  # data1
@pytest.mark.parametrize('data', yaml_load.load('../../resources/data/order.yaml').values())
def test4(data):
    print('***********获取到的yaml对象：' + str(
        data))  # {'errmsg': '保存成功1', 'status': 200}/{'errmsg': '保存成功2', 'status': 200}
    '''
    1、json.dumps：将“python数据结构”转换为“json字符串”
    2、ensure_ascii=False：解决中文乱码，只要加入参数ensure_ascii=False即可，这样json在序列化的时候，就不会使用默认的ASCII编码（这个是因为json在进行序列化时，默认使用的是编码是ASCII，而中文为Unicode编码，ASCII中不包含中文，所以出现了乱码）
    '''
    names = json.dumps(data['errmsg'], ensure_ascii=False)
    print('***********获取到的yaml值：' + names)
@pytest.mark.parametrize("data", yaml_load.load('../../resources/data/order.yaml').values())
def test5(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize("data", yaml_load.load('../../resources/data/order.yaml').values())
def test6(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize('data', yaml_load.load('../../resources/data/order1.yaml').values())
def test7(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize('data', [{'errmsg': '保存成功1', 'status': 200}, {'errmsg': '保存成功2', 'status': 300}])
def test_case2(data):
    print('获取到的yaml对象：' + str(data))  # 读取到的是列表中的一个值：{'errmsg': '保存成功1', 'status': 200}
    names = json.dumps(data['errmsg'], ensure_ascii=False)  # 由于读取到的列表中的值是一个dit，所以要使用对应的键去读取该键对应的值：保存成功1
    print('获取到的yaml值：' + names)
@pytest.mark.parametrize('data', [{'errmsg': '保存成功1', 'status': 200}, {'errmsg': '保存成功2', 'status': 300}])
def test15(data):
    print(data)
    print(json.dumps(data['status']))
    print(json.dumps(data['errmsg'][1]))
@pytest.mark.parametrize('data', ['name', '你好'])
def test_case3(data):
    print('获取到的yaml对象：' + str(data))  # 读取到的是列表中的一个值：name
    names = json.dumps(data[0], ensure_ascii=False)  # 由于读取到的列表中的值是一个str，所以根据下标读取的是字符串中的一个字符
    print('获取到的yaml值：' + names)
@pytest.mark.parametrize('datas', ['name', 'lilie', '5', 'male'])
def test(datas):
    print(datas)
    print(json.dumps(datas[0]))
@pytest.mark.parametrize('datas', ['name', 'lilie', '5', 'male'])
def test1(datas):
    print(datas)
@pytest.mark.parametrize('data', ['123', '345', '2356'])
def test(data):
    print(data)
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case4(data):
    print('1111111111111' + str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case5(data):
    print(str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case6(data):
    print(str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case7(data):
    print(str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case8(data):
    print(str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test_case9(data):
    print(str(data))
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml'))
def test_case10(data):
    print(str(data))
'''
{'errmsg': '保存成功1', 'status': 200}
{'errmsg': '保存成功2', 'status': 200}
{'errmsg': '保存成功3', 'status': 200}
'''
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test11(data):
    print(data)
@pytest.mark.parametrize('data', yaml_load.load2('../../resources/data/order.yaml').values())
def test12(data):
    print(data)
@pytest.mark.parametrize('datas', yaml_load.load2('../../resources/data/order.yaml').values())
def test13(datas):
    print(datas)
@pytest.mark.parametrize('datas', yaml_load.load2('../../resources/data/order.yaml').values())
def test14(datas):
    print(datas)
'''
Order1:
  errmsg: '保存成功1'
  status: 200
Order2:
  errmsg: '保存成功2'
  status: 200
Order3:
  errmsg: '保存成功3'
  status: 200
'''
@pytest.mark.parametrize('datas', yaml_load.load2('../../resources/data/order.yaml'))
def test15(datas):
    print(datas)  # Order1
'''
Order1:
  errmsg: '保存成功1'
  status: 200
Order2:
  errmsg: '保存成功2'
  status: 200
Order3:
  errmsg: '保存成功3'
  status: 200
'''
@pytest.mark.parametrize('datas', yaml_load.load2('../../resources/data/order.yaml').values())
def test16(datas):
    print(datas)  # {'errmsg': '保存成功1', 'status': 200}
@pytest.mark.parametrize("data", yaml_load.load('../../resources/data/order.yaml').values())
def test17(data):
    print(data)
    name = json.dumps(data['errmsg'], ensure_ascii=False)
    print(name)
@pytest.mark.parametrize('datas',yaml_load.load2('../../resources/data/order.yaml').values())
def test18(datas):
    print(data)
def load(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    print(data)
@pytest.mark.parametrize('datas',yaml_load.load('../../resources/data/order.yaml').values())
def test19(datas):
    print(datas)
@pytest.mark.parametrize('data', yaml_load.load('../../resources/data/order.yaml').values())
def test20(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize("data", yaml_load.load('../../resources/data/order.yaml').values())
def test21(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize('data', yaml_load.load('../../resources/data/order.yaml').values())
def test22(data):
    print(json.dumps(data['errmsg'], ensure_ascii=False))
@pytest.mark.parametrize('datas', yaml_load.load('../../resources/data/order.yaml').values())
def test23(datas):
    print(datas)
@pytest.mark.parametrize('datas',yaml_load.load2('../../resources/data/order.yaml').values())
def test24(datas):
    print(datas)
def load3(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas', load3('../../resources/data/order.yaml').values())
def test25(datas):
    print(datas)
    print(json.dumps(datas['status'],ensure_ascii=False))
def load4(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load4('../../resources/data/order.yaml').values())
def test26(datas):
    print(datas)
    print(json.dumps(datas['status'],ensure_ascii=False))
def load5(path):
    file=open(path,'r',encoding='utf-8')
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize("datas",load5('../../resources/data/order.yaml').values())
def test27(datas):
    print(datas)
    print(json.dumps(datas['status'],ensure_ascii=False))
def load6(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas', load6('../../resources/data/order.yaml').values())
def test28(datas):
    print(datas)
def load7(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load7('../../resources/data/order.yaml').values())
def test29(datas):
    print(datas['errmsg'])
def load8(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load8('../../resources/data/order.yaml').values())
def test30(datas):
    print(datas['errmsg'])
def load9(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load9('../../resources/data/order.yaml').values())
def test31(datas):
    print(datas)
    print(json.dumps(datas['errmsg'],ensure_ascii=False))
'''
练习：2025/3/20（1）
'''
def load10(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load10('../../resources/data/order.yaml').values())
def test32(datas):
    print(datas)
    print(json.dumps(datas['errmsg'],ensure_ascii=False))
def load33(path):
    file1=open(path,'r',encoding='utf-8')
    data=yaml.load(file1,Loader=yaml.FullLoader)
    return data
@pytest.mark.parametrize('datas',load33('../../resources/data/order.yaml').values())
def test34(datas):
    print(datas)