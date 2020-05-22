# -*- coding:utf-8 -*-
from mysql import connector
from API_C.Common.public.read_ini import configuration
from API_C.Common.public import project_path
class doMysql:
    '''这是一个数据库查询的类'''
    def select_mysql(self,query,flag):
        '''链接数据库'''
        db_future=configuration(project_path.config_path).read_else('DBCONFIG','db_data')
        dict=connector.connect(**db_future)
        '''获取游标，获取操作权限'''
        cursor=dict.cursor()
        '''操作数据库,查询标ID'''
        cursor.execute(query)
        if flag==1:
            res=cursor.fetchone()
        else:
             res=cursor.fetchall()
        db_future.close()
        return res
print(doMysql().select_mysql('select max(id) from loan where MemberID=666666',1))