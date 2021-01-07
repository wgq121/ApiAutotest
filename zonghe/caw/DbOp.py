'''
数据库操作
'''

import pymysql


# 连接数据库
def connect(db):
    '''
    连接数据库
    :param db: 字典格式的数据.db={"ip":"192.168.150.222","port":"4406","user":"root","pwd":"123456","dbname":"future"}
    :return: 连接对象
    '''
    # 从字典中取出相关的值
    ip = db['ip']
    port = db['port']
    user = db['user']
    pwd = db['pwd']
    name = db['dbname']
    try:
        conn = pymysql.connect(host=ip, user=user, password=pwd,
                               database=name, port=int(port),
                               charset='utf8')
        print(f"连接数据库{ip}:{port}成功。")
        return conn
    except Exception as e:
        print(f"连接数据库异常，异常信息为：{e}")


def disconnect(conn):
    try:
        conn.close()
        print("断开数据库连接成功。")
    except Exception as e:
        print(f"断开数据库连接异常，异常信息为：{e}")


def execute(conn, sql):
    try:
        # 获取游标
        c = conn.cursor()
        # 执行sql语句
        c.execute(sql)
        # 提交事务
        conn.commit()
        c.close()
        print(f"执行{sql}语句成功。")
    except Exception as e:
        print(f"执行{sql}语句异常，异常信息为：{e}。")


# if __name__ == '__main__':
#     db = {"ip": "192.168.150.222", "port": "4406", "user": "root", "pwd": "123456", "dbname": "future"}
#     conn = connect(db)
#     print(conn)
#     # 根据手机号删除用户
#     execute(conn, "delete from member where MobilePhone=13796996157")
#     disconnect(conn)
