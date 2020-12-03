# -*- codeing = utf-8 -*-
# @Time : 2020/12/1 21:23
# @Author : 张凯峰
# @File :zkf.py
# @Software: PyCharm

import pymysql
#向数据库中插入数据
def insert_db(id,buying,maint,doors,persons,lug_boot,safety):
    db = pymysql.connect('localhost', 'root', '1997', 'car')
    cursor = db.cursor()
    sql = "insert into car.car(id,buying,maint,doors,persons,lug_boot,safety) values ('%s','%s','%s','%s','%s','%s','%s')" %(id,buying,maint,doors,persons,lug_boot,safety)
    try:
        cursor.execute(sql)
        db.commit()
        print('数据插入成功！')
    except:
        print('数据插入失败！')
    db.close()

#打印数据库中所有数据
def display_db():
    db = pymysql.connect('localhost', 'root', '1997', 'car')
    cursor = db.cursor()
    sql = "select * from car.car"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            buying = row[1]
            maint = row[2]
            doors = row[3]
            persons = row[4]
            lug_boot = row[5]
            safety = row[6]
            print("id: '%s',buying: '%s',maint: '%s',doors: '%s',persons:'%s',lug_boot: '%s',safety:'%s'" % (id,buying,maint,doors,persons,lug_boot,safety))
        print("查询全部数据成功!")
    except:
        print('没有查询到全部数据！')
    db.close()

#数据库的查找
def query_db(name):
    db = pymysql.connect('localhost', 'root', '1997', 'car')
    cursor = db.cursor()
    sql = "select * from car.car where id = '%s' " % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            buying = row[1]
            maint = row[2]
            doors = row[3]
            persons = row[4]
            lug_boot = row[5]
            safety = row[6]
        print("id: '%s',buying: '%s', maint: '%s',doors: '%s',persons:'%s',lug_boot: '%s',safety:'%s'" % ( id , buying , maint , doors, persons, lug_boot, safety))
        print('查询成功!')
    except:
        print('没有查到数据!')
    db.close()

#更新数据库
def update_db(id,buying,maint,doors,persons,lug_boot,safety):
    db = pymysql.connect('localhost', 'root', '1997', 'car')
    cursor = db.cursor()
    sql = "update car.car set id = '%s', buying = '%s',maint = '%s',doors = '%s',persons = '%s', lug_boot = '%s',safety = '%s' where id = '%s'" %(id,buying,maint,doors,persons,lug_boot,safety,id)
    try:
        cursor.execute(sql)
        db.commit()
        print('修改成功!')
    except:
        print('修改失败!')
    db.close()

#数据库的删除
def delete_db(fg):
    db = pymysql.connect('localhost', 'root', '1997', 'car')
    cursor = db.cursor()
    sql = "delete from car.car where id = '%s'" % fg
    try:
        cursor.execute(sql)
        db.commit()
        print('删除数据库中的数据成功!')
    except:
        print('删除数据失败！')
    db.close()

#实现switch-case语句
class switch(object):
     def __init__(self, value):
         self.value = value
         self.fall = False

     def __iter__(self):
         """Return the match method once, then stop"""
         yield self.match
         raise StopIteration

     def match(self, *args):
         """Indicate whether or not to enter a case suite"""
         if self.fall or not args:
             return True
         elif self.value in args:  # changed for v1.5, see below
             self.fall = True
             return True
         else:
             return False

#建立一个car类
class data:
     #构造函数
     def __init__(self, id,buying,maint,doors,persons,lug_boot,safety):
         self.next = None
         self.id = id
         self.buying = buying
         self.maint = maint
         self.doors = doors
         self.persons = persons
         self.lug_boot = lug_boot
         self.safety = safety
     def show(self):
         print('id:',self.id, ' ', 'buying:', self.buying, ' ', 'maint:', self.maint, ' ', 'doors:', self.doors, ' ', 'persons:', self.persons,' ','lug_boot:',self.lug_boot,' ','safety:', self.safety,)

#建立一个列表类
class car:
     #构造函数
     def __init__(self):
         self.head = data('', 0, 0, 0, 0, 0, 0)
     #输出数据库中所有的数据
     def display(self):
         display_db()
     #新增car数据
     def insert(self):
         id = input("id:")
         buying = input("buying:")
         maint = input('maint:')
         doors = input('doors:')
         persons = input('persons:')
         lug_boot = input('lug_boot:')
         safety = input('safety:')
         insert_db(id, buying,maint,doors,persons,lug_boot,safety)
     #修改car数据
     def update(self):
         name = input('please enter you want to update:')
         query_db(name)
         id = input("id:")
         buying = input("buying:")
         maint = input('maint:')
         doors = input('doors:')
         persons = input('persons:')
         lug_boot = input('lug_boot:')
         safety = input('safety:')
         update_db(id, buying,maint,doors,persons,lug_boot,safety)
     #查询car数据
     def query(self):
         id = input('please enter the car you want to query:')
         query_db(id)

     #删除car数据
     def delete(self):
         id = input("please enter the car you want to delete:")
         delete_db(id)

def menu():
         print('*' * 100)
         print('       数据库操作           ')
         print("       输入'a'是将数据插入数据库")
         print("       输入'b'将显示数据库中的所有数据")
         print("       输入'c'将查询数据库中的指定信息")
         print("       输入'd'是删除数据库中数据")
         print("       输入'e'是修改数据库中数据")
         print('*' * 100)
#主函数，程序的入口
def main():
    stulist1 = car()
    menu()
    user_input = input('please enter the OPcode:')
    while user_input:
        print("a--insert/b--display/c--query/d--delete/u--update/p--basketball/--default")
        for case in switch(user_input):
            if case('a'):  # 按下'a'键
                stulist1.insert()
                user_input = input('please enter the OPcode:')
                break
            if case('b'):  # 按下'b'键
                menu()
                stulist1.display()
                user_input = input('please enter the OPcode:')
                break
            if case('c'):  # 按下'c'键
                stulist1.query()
                user_input = input('please enter the OPcode:')
                break
            if case('d'):  # 按下'd'键
                stulist1.delete()
                user_input = input('please enter your OPcode:')
                break
            if case('e'):  # 按下'e'键
                stulist1.update()
                user_input = input('please enter your OPcode:')
                break

if __name__ == "__main__":
    main()