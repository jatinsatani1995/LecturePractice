def findmaximum(num1, num2, num3):
    return max(num1, num2, num3)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

maximumnumber = findmaximum(number1, number2, number3)
print("The maximum of the three numbers is:", maximumnumber)
