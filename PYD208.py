#2進位: 0, 1
#10進位: 0,1,2,3,4,5,6,7,8,9
#16進位: 0-9 A(10), B(11), C(12) D(13), E(14), F(15)

num = eval(input())

if num==15:
    print("F")
elif num==14:
    print("E")
elif num==13:
    print("D")
elif num==12:
    print("C")
elif num==11:
    print("B")
elif num==10:
    print("A")
else:
    print(num)
    

