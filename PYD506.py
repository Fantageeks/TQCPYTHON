# TODO

def compute(a, b, c):
    tmp = b**2-4*a*c
    if tmp==0:
        sol = -b/(2*a)
        sol = str(sol)
    elif tmp<0:
        sol = "Your equation has no root."
    else:
        x1 = (-b+tmp**0.5)/(2*a)
        x2 = (-b-tmp**0.5)/(2*a)
        sol = str(x1)+", "+str(x2)
        
    return sol


num1 = int(input())
num2 = int(input())
num3 = int(input())

ans = compute(num1, num2, num3)
print(ans)