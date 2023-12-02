Age=int(input("Enter Your Age : "))

if Age>0 and Age<14:
    print("You Are Child")
elif Age>14 and Age<18:
    print("You Are Teenager")
elif Age>18 and Age<30:
    print("You Are Young")
elif Age>30 and Age<55:
     print("You Are Middle Age")
else:
    print("You Are Old")