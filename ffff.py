def add_numbers( a ,  b ):
    sum = a + b
    return sum
    
def sub_numbers( a ,  b ):
    sub = a - b
    return sub

def mul_numbers( a ,  b ):
    mul = a * b
    return mul

def div_numbers( a ,  b ):
    div = a / b
    return div


print("1..Addition of two number")
print("2..Subtraction of two number")
print("3..multiplication of two number")
print("4..division of two number")

choice=int(input("Enter Choice for input(1/2/3/4):"))

if choice>=5:
         print("Invalid input. Please enter a valid option.")
else:
    num1=int(input("Enter number1:"))
    num2=int(input("Enter number2:"))

    if choice==1:
         print("sum is two number is: " ,add_numbers(num1,num2))
    elif choice==2:
        print("subtraction is two number is: " ,sub_numbers(num1,num2))
    elif choice==3:
        print("multiplcation is two number is: " ,mul_numbers(num1,num2))
    elif choice==4:
        print("division is two number is: " ,div_numbers(num1,num2))
    else:
        print("Enter InValid Choice")
    
