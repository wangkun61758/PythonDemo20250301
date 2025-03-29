import pytest

'''
1、前提是安装插件：pytest-ordering（未安装执行顺序不会生效，且执行脚本不会进行报错提示）
2、先执行有排序的，执行完所有有排序的，再去执行无排序的函数（所以 @pytest.mark.skip(reason="没有原因的跳过") 在最后面执行）
3、两个函数排序相同，则在前面的先执行
'''
@pytest.mark.skipif(1==2,reason='没有原因的跳过')
def test1():
    print('打印没有原因的跳过')

@pytest.mark.skip(reason='没有原因的跳过')
def test2():
    print('打印没有原因的跳过')

@pytest.mark.skipif(1==2,reason='没有原因的跳过')
class Test():
    @pytest.mark.skipif(1 == 2, reason='没有原因的跳过')
    def test1(self):
        print('test1打印没有原因的跳过')

    @pytest.mark.skip(reason='没有原因的跳过')
    def test2(self):
        print('test2打印没有原因的跳过')


@pytest.mark.run(order=2)
def test_case1():
    print('第2个执行')


@pytest.mark.run(order=1)
def test_case2():
    print('第1个执行')


@pytest.mark.skip(reason="没有原因的跳过")
def test_case3():
    print('打印没有原因的跳过')


@pytest.mark.run(order=1)
def test_case4():
    print('第4个执行')


@pytest.mark.run(order=5)
def test_case5():
    print('***')


@pytest.mark.run(order=6)
def test_case6():
    print('@@@@')


@pytest.mark.run(order=7)
def test_case():
    print('!!!!!!!!')


@pytest.mark.run(order=5)
def test():
    print('22222222')


@pytest.mark.run(order=1)
def test3():
    print("运行")

@pytest.mark.run(order=2)
def test4():
    print("4")

@pytest.mark.run(order=3)
def test5():
    print("5")

@pytest.mark.run(order=6)
def test6():
    print("6")

@pytest.mark.run(order=7)
def test7():
    print("7")

@pytest.mark.run(order=8)
def test8():
    print('8')

@pytest.mark.run(order=9)
def test9():
    print('9')

@pytest.mark.run(order=10)
def test10():
    print('10')

