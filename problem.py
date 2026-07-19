def smallerNumberThanCurrent (num):
    result=[]

    for i in range(len(num)):
     count = 0 
     for j in range(len(num)):
        if num[j] <num[i] :
            count += 1
     result.append(count)

    return result


num =[8,1,2,2,3]
print(smallerNumberThanCurrent (num))