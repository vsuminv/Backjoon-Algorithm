num = []
a = 0
for i in range(9):
    n = int(input())
    num.append(n)
    if num[i] == max(num):
        a = i+1
print(max(num))
print(a)

    