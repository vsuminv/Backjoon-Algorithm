N = int(input())
nums = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in range(len(nums)):
    if nums[i] == v:
        cnt += 1
print(cnt)