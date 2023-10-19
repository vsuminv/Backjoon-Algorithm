N = int(input())
call = list(map(int, input().split()))
cnt = 0 
y = 0
z = 0

for i in range(N):
    a = int(call[i]/30)
    b = int(call[i]/60)
    if a <= 0:
        y += 10
    else :
        y += 10 * a + 10

    if b <= 0:
        z += 15
    else:
        z += 15 * b + 15
        
if y > z :
    print("M", z)
elif y < z :
    print("Y", y)
else:
    print("Y M", y)