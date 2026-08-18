nums = list(map(int,input("Enter the list:")))
maximum = nums[0]

for num in nums:
    if num > maximum:
        maximum = num

print(maximum)
