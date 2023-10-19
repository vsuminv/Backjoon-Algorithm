sum = 0
cnt = 0
n = []
for i in range(7):
    num = int(input())
   
    if num % 2 == 1 :
         n.append(num)
         sum += num
    else:
        cnt += 1

if cnt == 7:
    sum = -1
    print(sum)
else:
    print(sum)
    print(min(n))
    


        
