print("Wlcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0
if height >= 120:
    age = int(input("what is your age?\n"))
    if age < 12:
        bill += 5
        print(f"you have to pay $ {bill}")
    elif 12 > age < 18:
        bill += 7
        print(f"You have to pay $ {bill}")
    else:
        bill += 12
        print(f"You have to pay $ {bill}")
    photos = input("Do you want a photos of your self? Y/N \n ").title()
    if photos == "Y":
        bill += 3
        print(F"You have to pay $ {bill}\nThank you!")
    else:
        bill == bill
        print(f"You have to pay $ {bill}\n Thank you!")

    
else:
    print("Sorry!, you have to grow taller before you can ride.")