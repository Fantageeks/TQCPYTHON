"""
輸入四個單字 (ok)
欄寬為10、欄與欄間隔一個空白字元 (ok)
每列印兩個的方式(ok)
先列印向右靠齊 (ok)
再列印向左靠齊 (ok)
左右皆以直線 |（Vertical bar）作為邊界。

"""
# print(f"|{} {}|")

a = input()
b = input()
c = input()
d = input()

print(f"|{a:>10} {b:>10}|")
print(f"|{c:>10} {d:>10}|")
print(f"|{a:<10} {b:<10}|")
print(f"|{c:<10} {d:<10}|")