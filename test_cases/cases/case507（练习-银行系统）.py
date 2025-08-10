#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 10:26
=================================================='''
means = [0, 0, 0]  # [存款、理财、负债]
'''
1、打印开办理的业务
'''


def init():
    print()
    print('''以下为可办理的业务：
        1. 查询资产
        2. 存款
        3. 取款
        4. 计算复利
        q. 退出''')


# init()

'''
2、选择要办理的业务代码
'''


def main():
    init()
    while True:
        choice = input("请输入您要办理的业务代码: ")
        #  2.1、查询余额
        if choice == "1":
            balance()
        # 2.2、存款
        elif choice == "2":
            amount = float(input("请输入存款金额: "))
            saving(amount)
        # 2.3、取款
        elif choice == "3":
            draw = float(input("请输入取款金额: "))
            draw_money(draw)
        # 2.4、计算复利（定投）
        elif choice == "4":
            # 2.4.1、输入相应的复利计算的参数
            investment = float(input("请输入每月定投金额: "))
            annual_rate = float(input("请输入年收益率: "))
            years = int(input("请输入定投期限(年): "))

            # 2.4.2、判断输入的条件是否满足计算公式
            if investment <= 0 or annual_rate <= 0 or years <= 0:
                print("输入的数据有误")
            else:
                # 计算复利（定投）
                earnings(investment, annual_rate, years)
        # 2.5、退出
        elif choice == "q":
            print("欢迎下次光临！再见！")
            break
        else:
            print("你输入的指令有误，请重新输入\n")


'''
2.1、查询资产
'''


def balance():
    total = 0
    for i in means:
        total += i
    print("你的资产总额为：%.2f" % total)
    print("你的资产明细为：\n")
    print("存款：%.2f" % means[0])  # %前是格式（%.2f：占位符+精确位数），%后是数字
    print("理财：%.2f" % means[1])
    print("负债：%.2f" % means[2])


'''
2.2、存款
'''


def saving(amount):
    if amount < 0:
        print("存款金额不可小于 0！")
    else:
        means[0] = means[0] + amount
        print("已存款：%.2f 元" % amount)  # 已存款：100.00 元
        print("当前余额：%.2f 元" % means[0])


'''
2.3、存款
'''


def draw_money(draw):
    global means
    if draw < 0:
        print("取款金额不可小于 0！")
    elif draw > means[0]:
        print("取款金额不可超过余额！")
    else:
        means[0] = means[0] - draw  # 余额
        print("已取款： %.2f 元" % draw)  # 取款金额
        print("当前余额： %.2f 元" % means[0])


# 2.4、计算复利（定投）
def earnings(month_investment, annual_rate, years):
    annual_invest = 12 * month_investment  # “月定投金额”转换算成“年定投金额”
    annual__rate = annual_rate / 100  # 年收益率（转成百分制形式）
    if annual__rate == 0:
        earning = 0
    else:
        '''
        定投收益的计算公式为：M=a(1+x)[(1+x)^n-1]/x;
        其中M代表预期收益，a代表年定投金额，x代表年收益率，而n代表定投期数。
        假设用户每月定投金额为300元，一年也就是3600元，年收益率为15%，
        定投期限为35年，则可以计算出收益为3600(1+15%)[(1+15%)^35-1]/15%=3648044元。
        '''
        earning = annual_invest * (1 + annual__rate) * (pow((1 + annual__rate), years) - 1) / annual__rate
    print("定投的预期收入为: %.2f" % earning)
    means[1] = means[1] + earning
    print('此时理财总收入为：%.2f' % means[1])
    means[1] = earning


if __name__ == '__main__':
    main()
