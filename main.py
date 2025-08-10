import pytest

if __name__ == '__main__':
    '''
    1、./test_cases/cases/  执行的脚本路径
    2、pytest.main()中添加了要运行的脚本的路径后，pytest.ini中不需要设置 testpaths =./test_cases/cases_main/
    '''
    pytest.main()



