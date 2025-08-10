"""一个可用于表示汽车的类"""


# 1、声明一个类
class Car():

    # 1.1、定义类的初始化属性
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 1000  # 里程表

    # 1.2.1、定义类中的函数
    def get_descriptive(self):
        long_name = self.brand + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()

    # 1.2.2、定义类中的函数
    def read_odometer(self):
        print(self.brand + str(self.odometer_reading) + ' 的里程')


# 2.1、实例化一个对象
my_car = Car('特斯拉', 'model s', 2016)

