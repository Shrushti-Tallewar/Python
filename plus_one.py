nums = [1,2,3]

string = int("".join(map(str,nums)))         #converting to string by using str then again into int so that 1 can be added the to again list
result = string + 1
digit = [int(d) for d in str(result)]
print(digit)

