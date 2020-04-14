import random

answer = int(random.randint(1,10))
#answer = 10

while True:
    print("予想する数字を入力してください ",end='')
    temp = int(input())
    if answer == temp:
        print("Bingo")
        print("答えは%i" %answer)
        break
    elif temp >answer :
        print("Bigger")
    else :
        print("Smaller!!")