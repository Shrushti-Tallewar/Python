while True :
 try:
  a = int(input("Enter 1st number :"))
  b = int(input("Enter 2nd number :"))
 except ValueError:
    print ("something went wrong")
    break

 print("Available Operations \n1.Addition \n2.Substraction\n3.Multiplication\n4.Division")

 c =int(input("Enter the number of the operation:"))

 if c == 1 :
    print (a+b)
 elif c == 2 :
    print (a-b)
 elif c == 3:
    print (a*b)
 else  :
    print (a/b)

