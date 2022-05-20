# for loop: 可以計算出來重複的次數
# while: 迴圈+條件判斷+不一定可得知次數 = 不定數

#先取得第一個資料存入變數
#建立迴圈成立條件
#迴圈內執行的指令寫出
#先取得下一個資料存入變數

mylist = []
num = int(input())

while num!=9999:
    mylist.append(num)
    num = int(input())
    
print(min(mylist))