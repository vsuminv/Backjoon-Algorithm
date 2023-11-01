N = int(input())

for i in range(N):
    for k in range(int((2*N-1)/2), i,-1):
        print(' ',end = '')
    for j in range(int((2*N-1)/2)-i,int((2*N-1)/2)+i+1):
        print("*",end = '')
    print()
for j in range(N-1,0,-1):
    print(' '*(N-j)+'*'*(2*j-1))