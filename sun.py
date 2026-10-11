# FOR ADJACENT NUMBERS ONLY

# nums = [11,7,2,8,1]
# target = 9

# start = 0
# for i in range(1,len(nums)):
#     if nums[start] + nums[i]== target:
#         print([start,i])
#     start+=1

#CHECKING ALL THE NUMBERS OF LIST WITH SINGLE NUMBER

nums=[11,7,2,-2,8,1]
target = 9

for i in range ( len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]+nums[j]== target:
            print([i,j])