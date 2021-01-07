import requests
import pytest

@pytest.fixture(params=[{"mobilephone": "15006007018", "pwd": "123456", "regname": "", "code": "20110"},
                        {"mobilephone": "", "pwd": "85846215", "regname": "", "code": "20103"},
                        {"mobilephone": "15006008111", "pwd": "", "regname": "", "code": "20103"},
                        {"mobilephone": "", "pwd": "", "regname": "", "code": "20103"},
                        {"mobilephone": "18006007167", "pwd": "", "regname": "丫丫", "code": "20103"},
                        {"mobilephone": "", "pwd": "aaa58585", "regname": "wawa", "code": "20103"},
                        {"mobilephone": "15060715011", "pwd": "aaa55", "regname": "", "code": "20108"},
                        {"mobilephone": "15060715012", "pwd": "abc", "regname": "", "code": "20108"},
                        {"mobilephone": "15060715012", "pwd": "aaaaaa1952154126415", "regname": "", "code": "20108"},
                        {"mobilephone": "1", "pwd": "aaa58585", "regname": "", "code": "20109"},
                        {"mobilephone": "136485", "pwd": "aaa58585", "regname": "", "code": "20109"},
                        {"mobilephone": "1234567890", "pwd": "aaa58585", "regname": "", "code": "20109"},
                        {"mobilephone": "12345678941012", "pwd": "aaa58585", "regname": "", "code": "20109"},
                        {"mobilephone": "11111111111", "pwd": "aaa58585", "regname": "", "code": "20109"},
                        {"mobilephone": "15006007018", "pwd": "aaa58585", "regname": "", "code": "20110"}])
# request 是pytest中的关键字，固定写法
def register_data(request):
    # 通过request.param返回每一组数据，固定写法
    return request.param


def test_register(register_data):
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": register_data['mobilephone'], "pwd": register_data['pwd'], "regname": register_data['regname']}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['code'] == register_data['code']
