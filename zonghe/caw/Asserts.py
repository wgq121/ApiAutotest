'''
断言
'''
import pytest_check as ck

# check(r.json(),login_data['expect'],"code,msg,status")
def check(r_json,expect,keys):
    '''
    校验r_json与expect中，相应key对应的value是否相同。
    :param r_json: r.json()
    :param expect: 预期结果
    :param keys: 校验的key列表，用逗号分隔：code,msg,status
    :return:
    '''
    ks = keys.split(',')
    for k in ks:
        # 根据key取r_json中的value
        real = r_json[k]
        # 根据key取rexpect中的value
        exp = expect[k]
        try:
            # assert str(real) == str(exp)
            ck.equal(str(real),str(exp))
        except Exception as e:
            print(f"响应信息：{r_json},预期信息：{expect},校验{k}失败。")
