class calculator:

    def additon(self,a,b):
        return a+b
    
    def subtraction(self,a,b):
        return a-b
    
    def multiplication(self,a,b):
        return a*b
    
    def division(self,a,b):
        return a/b

number1=int(input("Enter number1 : "))
number2=int(input("Enter number2 : "))

calci=calculator()

print("addition is ",calci.additon(number1,number2))
print("subtraction is ",calci.subtraction(number1,number2))
print("multiplication is ",calci.multiplication(number1,number2))
print("division is ",calci.division(number1,number2))