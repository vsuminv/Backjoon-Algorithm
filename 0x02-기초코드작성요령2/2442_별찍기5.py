N = int(input())
for i in range(0, N):
    for j in range(i, int((2*N-1)/2)):
        print(' ',end='')
    for k in range(int((2*N-1)/2)-i , int((2*N-1)/2)+i+1) :
        print("*",end = '')
    print()
  