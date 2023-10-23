import sys
N = int(input())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
x = int(input())

left = 0 
right = N-1
count = 0

while left < right:
    tmp = num[left] + num[right]
    if tmp == x:
        count += 1
        left+=1
    elif tmp > x:
        right -=1
    else:
        left +=1
print(count)


