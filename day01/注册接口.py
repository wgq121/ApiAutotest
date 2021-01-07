import requests
import day01.util

def register(url, cs, code):
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['code'] == code


if __name__ == '__main__':
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    code = ["20110", "20103", "20103", "20103", "20103", "20103","20108","20108","20108","20109","20109","20109","20109","20109","20110","20110"]

    ds = day01.util.GetCsv().get("D:\ApiAutoTest\day01\data.csv")
    cs = []
    for d in ds:
        cs.append({"mobilephone": d[0], "pwd": d[1]})

    for i in range(len(cs)):
        register(url, cs[i], code[i])
