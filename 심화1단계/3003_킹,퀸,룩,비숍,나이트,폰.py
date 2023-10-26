N = [1,1,2,2,2,8]
c = list(map(int, input().split()))
num = 0 
for i in range(len(N)):
    if N[i] != c[i]:
        if N[i] > c[i]:
            num =  N[i]- c[i]
            print(num, end = ' ')
        else:
            
            num =  -(c[i]-N[i])
            print(num, end = ' ')
    
    else:
        print(0, end = ' ')
