class demo():
    def __init__(self,name,age):
        self.name=name
        self.age=age

name=str(input("enter name: "))   
age=int(input("enter age: "))

ddd=demo(name,age)

print("name is: ",ddd.name)
print("age is: ",ddd.age)
        

# class demo():
#     x=int(input("enter number1 "))
#     y=int(input("enter number2 "))
#     z=x+y
    
# xx=demo()
# print(xx.z)