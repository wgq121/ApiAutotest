'''
用户模块接口
'''


def register(url, baserequests, data):
    '''
    注册接口
    :param url: 环境数据，比如：http://jy001:8081/
    :param baserequests: Baserequests的实例
    :param data: 注册的数据
    :return: 响应
    '''
    url = url + "futureloan/mvc/api/member/register"
    return baserequests.post(url, data=data)


def login(url, baserequests, data):
    '''
    登录接口
    :param url: 环境数据，比如：http://jy001:8081/
    :param baserequests: Baserequests的实例
    :param data: 注册的数据
    :return: 响应
    '''
    url = url + "futureloan/mvc/api/member/login"
    return baserequests.post(url, data=data)

def query(url, baserequests):
   '''
   查询接口
   :param url:环境数据，比如：http://jy001:8081/
   :param baserequests:Baserequests的实例
   :return:响应
   '''
   url = url + "futureloan/mvc/api/member/list"
   return baserequests.post(url)
