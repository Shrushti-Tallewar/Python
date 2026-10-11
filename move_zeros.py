nums = [0,1,0,3,12]

# n = len(nums)

# for i in range (n):
#     if nums[i]==0:
#         nums[n]=nums[i]
#         print(nums)
  
k = 0

for i in range(len(nums)):
    if nums[i]!= 0:
        nums[k]=nums[i]
        k+=1
while  k <len(nums):
        nums[k]= 0 
        k+=1
        
print(nums)