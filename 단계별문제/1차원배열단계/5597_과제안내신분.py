nums = []
number = []
for j in range(1, 31):
    number.append(j)
    
for i in range(28):
    n = int(input())
    nums.append(n)
    if nums[i] not in number:
        print(nums[i])