'''
读文件相关的方法
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取当前工程的路径
    :return:
    '''
    cp = os.path.realpath(__file__)
    # print(cp)  # D:\ApiAutoTest\zonghe\caw\DataRead.py
    cd = os.path.dirname(cp)
    # print(cd)  # D:\ApiAutoTest\zonghe\caw
    return os.path.dirname(cd) + "\\"  # D:\ApiAutoTest\zonghe\


def read_ini(file_path, key):
    '''
    读取ini配置文件
    :param file_path: 配置文件的路径
    :param key: key值
    :return: key对应的value
    '''
    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path)
    # env对应ini文件中的[env]
    return config.get("env", key)

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path = get_project_path() + file_path
    with open(file_path,"r",encoding="utf-8") as f:
        content = f.read()
        return yaml.load(content,Loader=yaml.FullLoader)

if __name__ == '__main__':
    get_project_path()
    url = read_ini(r"data_env\env.ini", "url")
    print(url)
    db = read_ini(r"data_env\env.ini", "db")
    print(db)
    print(type(db))
    # 解析变量原有类型
    db = eval(db)
    print(db)
    print(type(db))

    c = read_yaml(r"data_case/register_fail.yaml")
    print(c)