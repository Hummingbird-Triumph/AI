# -*- codeing = utf-8 -*-
# @Time : 2020/11/1 21:22
# @Author : 张凯峰
# @File :one.py
# @Software: PyCharm

import pandas as pd
from urllib.request import urlretrieve
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
        r_list = []
        for r in res:
            r_list.append(list(r))
        return r_list

    def select_car_onehot(self):
        con = self.get_mysql_con()
        cur = con.cursor()
        sql = "select * from car.data;"
        cur.execute(sql)
        res = cur.fetchall()
        r_list = []
        for r in res:
            r_list.append(list(r))
        return r_list


def load_data():
    col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    data = pd.read_csv("car.csv", names=col_names)
    return data


def convert2onehot(data):
    # covert data to onehot representation
    data_frame = pd.DataFrame(data=data)
    return pd.get_dummies(data_frame, prefix=data_frame.columns)


if __name__ == "__main__":
    mysql = Mysql()
    car_data = mysql.select_car()
    car_convert_data = convert2onehot(car_data)
    print(car_convert_data.head())
    print('-' * 64)
    car_onehot_data = mysql.select_car_onehot()
    car_onehot_convert_data = convert2onehot(car_data)
    print(car_onehot_convert_data.head())
