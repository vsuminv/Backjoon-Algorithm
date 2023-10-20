cnt,num = map(int,input().split())
number = list(map(int,input().split()))

for i in range(cnt):
    if number[i] < num:
        print(number[i], end = " ")
