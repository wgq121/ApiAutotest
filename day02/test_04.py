'''
测试前置和后置：fixture的方式（自定义测试前后置）
1.命名比较灵活，不用setup、teardown这种固定命名
2.使用方便，跨文件使用时，不用import
'''
import pytest

# 在普通的函数上面增加fixture的注解，表示是测试前置
# 在需要使用的地方，作为参数使用
@pytest.fixture()
def login():
    print("登录系统")
    # yield 之前是前置，之后是后置
    yield
    print("退出登录")

# autouse=True时，测试用例自动使用
@pytest.fixture(autouse=True)
def data():
    print("准备测试数据")

def test_query():
    print("测试查询功能，不需要用户登录")

# 使用时，将方法login作为参数
def test_add(login):
    print("测试添加功能，需要用户登录")

# 使用userfixtures注解。
@pytest.mark.usefixtures('login')
def test_delete():
    print("测试删除功能，需要用户登录")