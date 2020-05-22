# -*- coding:utf-8 -*-
import pymysql
from Common.Public import Project_path
from Common.Public.Read_Conf import DyConf


class DoMysql:
    def select_db(self, query, falg=1):
        '''这是一个查询数据库在函数
        query表示需要输入的查询语句
        falg表示需要显示的条数  1表示一条，2表示多条'''
        db_data = DyConf(Project_path.Conf_path).read_else('DBCONFIG', 'db_data')
        # 打开数据库连接
        db = pymysql.connect(**db_data)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(query)
        if falg == 1:
            # 使用 fetchone() 方法获取单条数据
            data = cursor.fetchone()
        else:
            # 使用 fetchall() 方法获取多条数据
            data = cursor.fetchall()
        db.close()
        return data


if __name__ == '__main__':
    DoMysql().select_db('select * from member ORDER BY MobilePhone desc limit 2 ', 2)