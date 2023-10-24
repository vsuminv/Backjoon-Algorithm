N = int(input())
M = int(input())

il = (M % 100)%10 
sib = int((M % 100) / 10)
bak = M // 100 

print(N*il)
print(sib*N)
print(bak*N)
print(M*N)