"""
1.輸入四個分別含有小數1到4位的浮點數(ok)
2.欄寬為7(ok)
3.欄與欄間隔一個空白字元(ok)
4.每列印兩個的方式(ok)
5.先列印向右靠齊，(ok)
6.再列印向左靠齊，左右皆以直線 (ok)
7.（Vertical bar）作為邊界。(ok)
8.小數點後第二位。
"""
# 尖尖地方向右，向右靠齊(>)
# 尖尖地方向左，向左靠齊(<)
# 尖尖地方向上，置中對齊(^) shift+6
# 格式化: 結構f"{變數:對齊 欄寬.小數點位數f}"

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(f"|{a:>7.2f} {b:>7.2f}|")
print(f"|{c:>7.2f} {d:>7.2f}|")
print(f"|{a:<7.2f} {b:<7.2f}|")
print(f"|{c:<7.2f} {d:<7.2f}|")



