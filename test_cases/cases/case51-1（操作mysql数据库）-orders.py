import random

import pymysql
from faker import Faker

# 初始化 Faker 实例（生成假数据）
fake = Faker('zh_CN')

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '360buyer',
    'database': 'wk',
    'port': 3306
}


# 生成测试数据（name, email）
def create_datas(counts):
    return [(random.randint(10000,99999), fake.name(),random.choice(['电视机','洗衣机','冰箱','空调']), fake.numerify(), random.randint(1000,9999),fake.date()) for _ in
            range(counts)]


# 批量插入数据
def insert_datas(data):
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # 批量插入 SQL
        sql = "INSERT INTO orders (orderNo, name,goods, count, price,createtime) VALUES (%s, %s,%s, %s, %s,%s);"
        cursor.executemany(sql, data)

        # 提交事务
        connection.commit()
        print(f"成功插入 {cursor.rowcount} 条数据")

    except pymysql.Error as e:
        print(f"数据库错误: {e}")
        connection.rollback()

    finally:
        # 关闭连接
        if 'connection' in locals():
            cursor.close()
            connection.close()


# 主程序入口
if __name__ == '__main__':
    # 生成 100 条测试数据
    sql_datas = create_datas(100)

    # 执行批量插入
    insert_datas(sql_datas)
