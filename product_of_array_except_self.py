nums = [1,2,3,4]
digit=[]
for i in range(len(nums)):
    new = 1 
    for j in range(len(nums)):
        if i != j:
           new = new * nums[j]
    digit.append(new)
print(digit)