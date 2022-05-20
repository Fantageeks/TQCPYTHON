

a = int(input())
b = int(input())
total = 0

for i in range(a, b+1): #產生所有的數字範圍
    if i%2==0:
        total += i #total= total+i
        
print(total)