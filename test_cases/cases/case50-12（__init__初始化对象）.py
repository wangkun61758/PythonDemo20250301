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

'''
 A.2、根据设置的loogging的属性（比如格式、颜色等），进行打印
'''


class Bike():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometers = 100

    def get_des(self):
        print(self.brand + self.model + str(self.odometers))


my_bike = Bike('哈弗', 'h6', 2022)


class Car1():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometers = 100

    def get(self):
        print(self.brand)


my_car = Car1('哈弗', 'h6', '2024')
my_car.get()


class Car2():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.model = 'su7'

    def des(self):
        print(self.brand, self.model, self.year)


my_car2 = Car2('小米', '2024')
my_car2.des()
