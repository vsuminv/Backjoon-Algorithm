N, M =map(int,input().split())
a = [0]*N
for z in range(M):
    i,j,k = map(int,input().split())
    for n in range(i,j+1):
        a[n-1] = k
for i in range(0, N):
    print(a[i], end = ' ')
    
        
        
        
    