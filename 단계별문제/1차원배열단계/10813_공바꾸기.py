N, M = map(int, input().split())
nums = []
tmp = 0
for l in range(1,N+1):
    nums.append(l)

for a in range(M):
    i,j = map(int, input().split())
    tmp = nums[i-1] 
    nums[i-1] = nums[j-1]
    nums[j-1] = tmp
for i in nums:
    print(i, end = ' ')
    

    
    