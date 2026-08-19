n = int(input("Enter the number of terms: "))

a, b, c = 0, 1, 1

print("Tribonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b, c = b, c, a + b + c
