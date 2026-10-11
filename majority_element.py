nums = [2,3,1,6,7,2]              # A majority has to be appear half times otherwise it wont be counted
nums = [2,1,2,3]
n = len(nums)
for i in nums:
    if nums.count(i) > n//2:
        print(i)
