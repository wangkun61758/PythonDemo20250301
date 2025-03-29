import os.path


def try_except():
    try:  # 1、要执行的代码块
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file:
            try:
                file.write("这是要写入文件的内容")
            finally:  # 退出try时总会执行
                print('关闭文件')
                file.close()

    # 2、1如果（代码块执行）发生了异常
    except IOError:  # IOError：输入/输出操作失败
        print("Error: 没有找到文件或读取文件失败")
    # 2、2如果（代码块执行）没有异常发生
    else:
        print("内容写入文件成功")
        file.close()

try_except()

# 定义函数
def temp_convert(var):
    try:  # 1、要执行的代码块
        return int(var)
    except ValueError as Argument:  # 2、如果（代码块执行）发生了异常
        print('参数没有包含数字:' + str(Argument))  # str(Argument)： invalid literal for int() with base 10: 'xyz'
# 调用函数
temp_convert("xyz")

def try_except1():
    try:
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file:
            try:
                file.write("写入的内容")
            finally:
                file.close()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print('文件写入成功')

def try_except2():
    try:
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file2:
            try:
                file2.write('写入的内容')
            finally:
                file2.close()

    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print('文件写入成功')

def try_except3():
    try:
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file3:
            try:
                file3.write('写入文件的内容')
            finally:
                file3.close()

    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print('文件写入成功')

def try_except4():
    try:
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file4:
           try:
                file4.write('写入的内容')
           finally:
               file4.close()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print('文件写入成功')

def try_except():
    try:
        if not os.path.exists('../../resources/yaml'):
            os.makedirs('../../resources/yaml')
        with open('../../resources/yaml/file.yaml', 'w', encoding='utf-8') as file5:
            try:
                file5.write('写入的内容')
            finally:
                file5.close()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print('文件写入成功')





