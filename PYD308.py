# TODO

n = int(input())

for _ in range(n):
    numstr = input() #數字字串，由字元構成
    total = 0
    for i in numstr:
        total += int(i)
    
    print(f"Sum of all digits of {numstr} is {total}")
        


"""
Sum of all digits of _ is _
"""