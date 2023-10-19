n = []
for i in range(5):
    num = int(input())
    n.append(num)
    
print(int(sum(n)/5))
n.sort()
print(n[2])

    