n1 = list(input())
n2 = list(input())

for i in range(len(n1)):
    for j in n2:
        if j in n1:
            n1.remove(j)
            n2.remove(j)
                
print(len(n1) + len(n2) )


