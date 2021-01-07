'''
pytest脚本
1.文件以test_ 开头
2.测试类以Test开头
3.测试函数或方法以test_开头
'''

import requests

url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"

def test_regsiter_001():
    cs = {"mobilephone": "15006007018", "pwd": "123456"}
    r = requests.post(url,data=cs)
    print(r.text)
    # assert r.json()['code'] == '20110'


def test_regsiter_002():
    cs = {"mobilephone": "15006007018", "pwd": "12345"}
    r = requests.post(url,data=cs)
    print(r.text)
    # assert r.json()['code'] == '20108'

def test_regsiter_003():
    cs = {"mobilephone": "150060070138", "pwd": "123456"}
    r = requests.post(url,data=cs)
    print(r.text)
    # assert r.json()['code'] == '20109'