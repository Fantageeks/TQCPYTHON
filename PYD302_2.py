a = int(input())
b = int(input())

if a%2==0:
    total = sum(range(a, b+1, 2))
else:
    total = sum(range(a+1, b+1, 2))
    
print(total)
    
