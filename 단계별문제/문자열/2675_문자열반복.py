T = int(input())

for i in range(T):
    w = ''
    R,S = map(str, input().split())
    R = int(R)
    for j in range(len(S)):
        w += S[j]*R
    print(w)
    