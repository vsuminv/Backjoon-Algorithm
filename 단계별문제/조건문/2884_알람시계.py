A, B = map(int, input().split())

if B - 45 < 60:
    B += 60 - 45
    A -=1
else :
    B -= 45
if A <= 0:
    A += 24
print(A ,B)