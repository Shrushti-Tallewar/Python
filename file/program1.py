nums = [2,4,6]

n = len(nums)
ans = []
ans = [nums[0]]
for i in range(1,n):
    x = ans[i-1]+nums[i]
    ans.append(x)

print(ans)
print(nums[0])