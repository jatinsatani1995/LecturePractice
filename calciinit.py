class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
       
    def addi(self):
        return self.a+self.b
    
    def subtraction(self):
            return self.a-self.b
    
    def multiplication(self):
            return self.a*self.b
        
    def division(self):
            return self.a/self.b
       

number1=int(input("Enter number1: "))
number2=int(input("Enter number2: "))

calci=calculator(number1,number2)

ch=1

while ch!=0:
    print("1 for additon")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    
    ch=int(input("Enter Choice: "))
    
    if ch==1:
       print("addition is ",calci.addi())
    elif ch==2:
        print("subtraction is ",calci.subtraction())
    elif ch==3:
        print("multiplication is ",calci.multiplication())
    elif ch==4:
        print("division is ",calci.division())
    elif ch==0:
         print("Exit")
    else:
        print("Please Enter Valid choice")
        
print()