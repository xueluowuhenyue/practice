import  pymysql
from Common.Public import project_path
from Common.Public.read_conf import configuration
class Dopymysql:
    def select_db(self,query,falg=1):
        '''这是一个查询数据库在函数
        query表示需要输入的查询语句
        falg表示需要显示的条数  1表示一条，2表示多条'''
        db_data=configuration(project_path.config_path).read_else('db_data','db_data')
        #打开数据库连接
        db=pymysql.connect(**db_data)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(query)
        if falg==1:
            # 使用 fetchone() 方法获取单条数据
            data=cursor.fetchone()
        else:
            # 使用 fetchall() 方法获取多条数据
            data=cursor.fetchall()
        db.close()
        return data


if __name__ == '__main__':
    Dopymysql().select_db('SELECT * from sms_db_02.t_mvcode_info_1',2)