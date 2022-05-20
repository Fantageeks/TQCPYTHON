# TODO

def compute(num):
    fib = [0, 1]
    for i in range(2, num):
        f= fib[i-1]+fib[i-2]
        fib.append(f)
    return fib

n = int(input())
ans = compute(n)


#（每個數值後方為一個半形空格）
mystr = ""
for num in ans:
    mystr=mystr+str(num)+" "

print(mystr)


