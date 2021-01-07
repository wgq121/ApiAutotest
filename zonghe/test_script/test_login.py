'''
  1.直接在测试脚本中实现以下步骤
  注册用户
  下发登录的请求
  检查结果
  删除注册的用户
  2.将注册用户与删除注册用户分别放到测试前后置中
'''
import pytest

from zonghe.baw import Db, Member
from zonghe.caw import DataRead, Asserts


@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture()
def register(setup_data, url, db, baserequests):
    mobilephone = str(setup_data['casedata']['mobilephone'])
    # print("电话号码：",mobilephone)
    # 初始化环境：删除注册的用户（数据库中可能有其他人测试的数据，与本次测试冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    Db.delete_user(db, mobilephone)


def test_login(register, login_data, url, baserequests):
    # 下发登录请求
    r = Member.login(url, baserequests, login_data['casedata'])
    # 检查结果
    print(r.text)

    Asserts.check(r.json(),login_data['expect'],"code,msg,status")
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['msg'] == login_data['expect']['msg']
    # assert r.json()['status'] == login_data['expect']['status']

