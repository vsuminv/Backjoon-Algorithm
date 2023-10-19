N = int(input())

for i in range(N):
    for j in range(i, int((2*N-1)/2)):
        print(" ",end = '')
    for k in range(int(2*N-1)-i,int(2*N-1)+i+1):
        print("*",end='')
    print()
for a in range(N-1,0,-1):
    print(" "*(N-a)+"*"*(2*a-1))