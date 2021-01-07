import requests


def login(url, cs, code):
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['code'] == code


if __name__ == '__main__':
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
    code = ["10001", "20103", "20103", "20103", "20111", "20111","20111","20111"]

    cs = [{"mobilephone": "18012345678", "pwd": "123456"},
          {"mobilephone": "18012345678", "pwd": ""},
          {"mobilephone": "", "pwd": "123456"},
          {"mobilephone": "", "pwd": ""},
          {"mobilephone": "18112345678", "pwd": "123456"},
          {"mobilephone": "123", "pwd": "123456"},
          {"mobilephone": "18012345678", "pwd": "aaa55"},
          {"mobilephone": "18012345678", "pwd": "abcddsa"},
         ]
    for i in range(len(cs)):
        login(url, cs[i], code[i])
