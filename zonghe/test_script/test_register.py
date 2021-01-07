'''
注册的测试脚本
'''
import pytest

from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


# pytest 数据驱动
# 从yaml中读取测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml("data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


def test_register_fail(url, baserequests, fail_data):
    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data['data'])
    # 断言结果
    print(r.text)
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Asserts.check(r.json(), fail_data['expect'], "code,msg,status")


# 把注册成功的数据写到register_pass.yaml
# 之策成功的脚本，下发请求，断言响应结果
def test_register_pass(url, baserequests, pass_data, db):
    mobilephone = str(pass_data['data']['mobilephone'])
    # 初始化环境：删除注册的用户（数据库中可能有其他人测试的数据，与本次测试冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    print(r.text)
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    Asserts.check(r.json(), pass_data['expect'], "code,msg,status")

    # 调用查询的接口，在查询的结果中能找到本次注册的手机号
    q = Member.query(url, baserequests)
    # print(eval(q.text)['data'])
    assert mobilephone in q.text
    # 清理环境：删除注册的用户
    Db.delete_user(db, mobilephone)


# 重复注册用例
def test_register_repeat(url, baserequests, pass_data, db):
    mobilephone = str(pass_data['data']['mobilephone'])
    # 初始化环境：删除注册的用户（数据库中可能有其他人测试的数据，与本次测试冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    print(r.text)
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    Asserts.check(r.json(), pass_data['expect'], "code,msg,status")

    # 调用查询的接口，在查询的结果中能找到本次注册的手机号
    q = Member.query(url, baserequests)
    # print(eval(q.text)['data'])
    assert mobilephone in q.text
    # 重复注册
    r = Member.register(url, baserequests, pass_data['data'])
    # print(r.text)
    # assert r.json()['code'] == pass_data['repeat']['code']
    # assert r.json()['msg'] == pass_data['repeat']['msg']
    # assert r.json()['status'] == pass_data['repeat']['status']
    Asserts.check(r.json(), pass_data['repeat'], "code,msg,status")

    # 清理环境：删除注册的用户
    Db.delete_user(db, mobilephone)
