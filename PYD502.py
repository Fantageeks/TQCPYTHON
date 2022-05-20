
#Step 1: define function
#x,y: 區域變數，只存活在compute函式中

def compute(x, y):
    return x*y #Step 3: 看到return，函式結束

#Main program starts:
num1 = int(input()) #input()字串型態資料，轉成整數型態
num2 = int(input())

#step 2: call function
ans = compute(num1, num2)
print(ans)