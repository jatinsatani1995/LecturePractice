class student:
   
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight


name1=str(input("Enter name: "))
age1=int(input("Enter age: "))
height1=float(input("Enter height: "))
weight1=float(input("Enter weight: "))

stinfo=student(name1,age1,height1,weight1)
print("\n")
print("name is: ", stinfo.name)
print("age is: ", stinfo.age)
print("height is: ", stinfo.height)
print("weight is: ", stinfo.weight)
    