# TODO

import math

def compute(x, y):
    ans = math.gcd(x,y)
    return ans

#字串的切割，以逗號為切割，切割完的結果會存到list中
#字串切完後，陣列中的元素還是字串
#把串列中的元素，每一個都用int對應，每一個都轉成整數
num1, num2 = map(int, input().split(",")) 
ans = compute(num1, num2)
print(ans)