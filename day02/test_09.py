'''
mark标记;
1.skip跳过用例不执行
2.自定义标记:接口自动化(api)、功能自动化(func)、界面自动化(ui)、冒烟测试(smoke)。
    通过自定义标记，标记用例属于哪一类。
    比如版本转测试，需要进行冒烟测试，只执行带有冒烟测试标记的用例。

    -m=smoke 执行带smoke标记的用例
    -m=func
    也可以使用逻辑表达式
    -m="smoke and func"
    -m="smoke or func"
    -m="not smoke"
'''
import pytest

version = 'V1R1'

@pytest.mark.smoke
def test_case01():
    print("用例1")

@pytest.mark.skip("跳过的原因：缺陷，改动比较大，作为以后版本的需求来实现。")
def test_case02():
    print("用例2")

@pytest.mark.skipif(version == 'V1R1', reason='不支持V1R1版本')
def test_case03():
    print("用例3")

@pytest.mark.func
def test_case04():
    print("用例4")

def test_case05():
    print("用例5")

# 对类下面的所有用例生效
@pytest.mark.func
class TestClass:

    @pytest.mark.smoke
    def test_case06(self):
        print("用例6")

    @pytest.mark.smoke
    def test_case07(self):
        print("用例7")

    def test_case08(self):
        print("用例8")

    def test_case09(self):
        print("用例9")

    def test_case10(self):
        print("用例10")
