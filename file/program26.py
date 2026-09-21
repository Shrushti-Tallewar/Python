running_total = 0

print("--- Starting Number Classification ---")

for number in range(1, 11):
    if number == 7:
      print(f"Number {number}: This is a lucky number!")
        
    elif number % 2 == 0:
        print(f"Number {number}: Even")
    else:
        print(f"Number {number}: Odd")
          
    running_total = running_total + number

print("--------------------------------------")
print(f"The sum of all numbers from 1 to 10 is: {running_total}")
