def primenum(number):
  
   if number %2 ==0 or number %3 ==0:
        return True  
    


num = int(input("Enter Number: "))
if not primenum(num):
    print("number is a prime number.")
else:
    print("number is not a prime number.")

    