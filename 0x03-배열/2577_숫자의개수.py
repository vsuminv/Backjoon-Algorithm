A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))
for i in range (10):
    count = 0
    for j in result:
        if  str(i) in j :
            count += 1
    print(count)