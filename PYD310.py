# TODO

n = int(input())
total = 0

#1, 2, 3, ....n-1
for i in range(1, n):
    total = total + 1/(i**0.5 + (i+1)**0.5)
    
print(f"{total:.4f}")