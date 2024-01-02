marks=[]
total=0

for i in range(5):
    marks.insert(i,input("Enter marks"))
    
for i in range(5):
    total=total+int(marks[i])
    
average=total/5


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
