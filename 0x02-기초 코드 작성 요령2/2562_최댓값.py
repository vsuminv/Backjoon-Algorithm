num = []
for i in range(9):
   n = int(input())
   num.append(n)
print(max(num))
for j in range(len(num)):
    if num[j] == max(num):
        print(j+1)
    