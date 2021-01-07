import requests
import pytest


@pytest.fixture(params=[{"data": {"mobilephone": "15006007018", "pwd": "123456", "regname": ""},
                         "expect": {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}},
                        {"data": {"mobilephone": "", "pwd": "123456", "regname": ""},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "手机号码已被注册"}}])
# request 是pytest中的关键字，固定写法
def register_data(request):
    # 通过request.param返回每一组数据，固定写法
    return request.param

def test_register(register_data):
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    assert r.json()['code'] == register_data['expect']['code']
