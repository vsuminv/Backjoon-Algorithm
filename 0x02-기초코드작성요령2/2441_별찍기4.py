N = int(input())
for i in range(1, N+1):
    for j in range(0, i-1):
        print(' ',end = '')
        # print(j,end ='')
    for k in range(i, N+1):
        print("*", end = '')
    print()