nums = []
for i in range(9):
    n = int(input())
    nums.append(n)
for j in nums:
    for k in nums:
        if sum(nums) - (j+k) == 100 and j != k:
            nums.remove(j)
            nums.remove(k)
nums.sort()

for l in nums:
    print(l)

