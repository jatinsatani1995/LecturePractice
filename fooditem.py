from datetime import datetime
data={}
final_amount=0
    
while True:
    a="RESTAURANT"
    print(a.center(40," "))
    print("""Code \t Food \t \t\t price
    1 \t Pizza \t \t\t 100
    2 \t Dhosa \t \t\t 200
    3 \t Chole Bhature \t \t 300
    4 \t Ice-Cream \t \t 400""")
    
    choice=int(input("Enter Choice :"))
    if choice==1:
        Quantity=int(input("Enter the quantity of Pizza:"))
        amount=100*Quantity
        final_amount+=amount
        if "Pizza" in data.keys():
            data["Pizza"]["quantity"]+=Quantity
            data["Pizza"]["amount"]+=amount
        else:
            data.update({"Pizza":{"quantity":Quantity,"amount":amount,}})
    elif choice==2:
        Quantity=int(input("Enter the quantity of Dhosa:"))
        amount=200*Quantity
        final_amount+=amount
        if "Dhosa" in data.keys():
            data["Dhosa"]["quantity"]+=Quantity
            data["Dhosa"]["amount"]+=amount
        else:
            data.update({"Dhosa":{"quantity":Quantity,"amount":amount,}})
    elif choice==3:
        Quantity=int(input("Enter the quantity of Chole Bhature:"))
        amount=300*Quantity
        final_amount+=amount
        if "Chole Bhature" in data.keys():
            data["Chole Bhature"]["quantity"]+=Quantity
            data["Chole Bhature"]["amount"]+=amount
        else:
            data.update({"Chole Bhature":{"quantity":Quantity,"amount":amount,}})
    elif choice==4:
        Quantity=int(input("Enter the quantity of Ice Cream:"))
        amount=400*Quantity
        final_amount+=amount
        if "Ice Cream" in data.keys():
            data["Ice Cream"]["quantity"]+=Quantity
            data["Ice Cream"]["amount"]+=amount
        else:
            data.update({"Ice Cream":{"quantity":Quantity,"amount":amount,}}) 
    else:
        print("please select your order")
    print(amount)
    print(final_amount)
    z = input("Enter yes/no to continue :")
    if z=="yes":
        continue
    elif z=="no":
        print(data)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        print("RESTAURANT NAME".center(50))
        print((datetime.today().strftime("%m/%d/%Y")).ljust(41),(datetime.today().strftime("%I:%M %p")).rjust(3))
        print("".center(50,"*"))
        all_keys=data.keys()
        for i in all_keys:
            k=data[i]["quantity"]
            a=data[i]["amount"]
            b=str(k)
            c=str(a)
            print(f"{i.ljust(15)}{b.center(15)} {c.rjust(15)}")
        print("\n")
        print("\n")
        print("\n")
        print("".center(50,"*"))
        print(f"Your Final Bill is {final_amount}".center(50))
        print("".center(50,"*"))
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")

        break
    else:
        print("Enter either yes/no")