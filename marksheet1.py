marks1=int(input("Enter Marks1: "))
marks2=int(input("Enter Marks2: "))
marks3=int(input("Enter Marks3: "))
marks4=int(input("Enter Marks4: "))
marks5=int(input("Enter Marks5: "))

totalmarks=marks1+marks2+marks3+marks4+marks5
average=totalmarks/5




if(marks1>=50 and marks2>=50 and marks3>=50 and marks4>=50 and marks5>=50):

    if average>=90 and average<=100:
        print("your grade is A1")
    elif average>=80 and average<90:
        print("your grade is A2")
    elif average>=70 and average<80:
        print("your grade is B1")
    elif average>=60 and average<70:
        print("your grade is B2")
    elif average>=50 and average<60:
        print("your grade is C1")
    else:
        print("You are Fail")
    print("your Percentage is: ",average)
else:
    print("you are fail")
    