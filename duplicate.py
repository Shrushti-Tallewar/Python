nums= [1,2,3,1]

if nums != list(set(nums)):
    print("True,there exists duplicates")
else:
    print("False,there dosent exists duplicates")


nums =[1,2,4,7,2,1]
unique=[]

for i in range (nums):
    if i not  in unique:
        unique.append(i)
print(unique)