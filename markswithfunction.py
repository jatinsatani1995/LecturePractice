def marksheet(m1,m2,m3,m4,m5):
    totalmarks=m1+m2+m3+m4+m5
    average=totalmarks/5
    
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
    return average


marks1=int(input("Enter Marks1: "))
marks2=int(input("Enter Marks2: "))
marks3=int(input("Enter Marks3: "))
marks4=int(input("Enter Marks4: "))
marks5=int(input("Enter Marks5: "))


print("your Percentage is: ",marksheet(marks1,marks2,marks3,marks4,marks5))