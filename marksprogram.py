Marks=int(input("Enter Your Marks: "))
if Marks<0:
    print("Please Enter Valid Marks")
elif Marks >=33 and Marks <=55:
     print("Your Grade is D")
elif Marks >=56 and Marks <=70:
     print("Your Grade is C")
elif Marks >=71 and Marks <=85:
     print("Your Grade is B")
elif Marks >=86 and Marks <=100:
     print("Your Grade is A")
else:
    print("You Are Fail")