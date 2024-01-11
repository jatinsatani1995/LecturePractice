class calci1:
    
    def additon(self,num1,num2):
        return num1+num2

class calci2:
    
    def subtraction(self,num1,num2):
        return num1-num2
    
class calci3:
    
     def multiplication(self,num1,num2):
            return num1*num2    
    
class calculator(calci1,calci2,calci3):
    
     def division(self,num1,num2):
            return num1/num2
        
number1=int(input("enter number1: "))
number2=int(input("enter number2: "))


finalcal=calculator()
print("Addition is: ", finalcal.additon(number1,number2))
print("subtraction is: ", finalcal.subtraction(number1,number2))
print("multiplication is: ", finalcal.multiplication(number1,number2))
print("division is: ", finalcal.division(number1,number2))
        