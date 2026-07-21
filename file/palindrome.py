x = int(input("enter the number:"))
temp = x
rev = 0

while temp > 0:
    r = temp % 10
    rev = rev * 10 + r
    temp //= 10

if rev == x :
    print("True")
else:
    print("False")


