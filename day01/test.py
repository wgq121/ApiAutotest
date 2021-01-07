import day01.util

ds = day01.util.GetCsv().get("D:\ApiAutoTest\day01\data.csv")
cs = []
for d in ds:
    cs.append({"mobilephone":d[0], "pwd":d[1]})
print(cs)

# data = day01.util.GetExcel.get("D:\ApiAutoTest\day01\data.xlsx","users")
# print(data)
#
# cs = [{"mobilephone": "15006007018", "pwd": "123456", "regname": ""},
#       {"mobilephone": "", "pwd": "85846215", "regname": ""},
#       {"mobilephone": "15006008111", "pwd": "", "regname": ""},
#       {"mobilephone": "", "pwd": "", "regname": ""},
#       {"mobilephone": "18006007167", "pwd": "", "regname": "丫丫"},
#       {"mobilephone": "", "pwd": "aaa58585", "regname": "wawa"},
#       {"mobilephone": "15060715011", "pwd": "aaa55"},
#       {"mobilephone": "15060715012", "pwd": "abc"},
#       {"mobilephone": "15060715012", "pwd": "aaaaaa1952154126415"},
#       {"mobilephone": "1", "pwd": "aaa58585"},
#       {"mobilephone": "136485", "pwd": "aaa58585"},
#       {"mobilephone": "1234567890", "pwd": "aaa58585"},
#       {"mobilephone": "12345678941012", "pwd": "aaa58585", },
#       {"mobilephone": "11111111111", "pwd": "aaa58585"},
#       {"mobilephone": "15006007018", "pwd": "aaa58585"},
#       {"mobilephone": "15006007018", "pwd": "aaa58585",
#        "regname": "弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟弟"}]
