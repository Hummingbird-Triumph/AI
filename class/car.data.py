# -*- codeing = utf-8 -*-
# @Time : 2020/11/27 15:47
# @Author : 张凯峰
# @File :car.data.py
# @Software: PyCharm


# 引入pymysql包
import pymysql


MYSQL_CONFIG = {
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': '1997',
    'DB': 'car',
    'CHARSET': 'utf8'
}


class Mysql():
    def __init__(self):
        self.host = MYSQL_CONFIG['HOST']
        self.port = MYSQL_CONFIG['PORT']
        self.user = MYSQL_CONFIG['USER']
        self.password = MYSQL_CONFIG['PASSWORD']
        self.db = MYSQL_CONFIG['DB']
        self.charset = MYSQL_CONFIG['CHARSET']

    def get_mysql_con(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )

    def select_car(self):
        con = self.get_mysql_con()
        cur = con.cursor()
        sql = "select * from car.data;"
        cur.execute(sql)
        res = cur.fetchall()
        return list(res)



if __name__ == "__main__":
    myql = Mysql()
    print(myql.select_car())
    print('-' * 64)

