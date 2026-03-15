
# simpleast format

print("Welcome to Python Pizza Deliveres!")

bill = 0 
size = input("What size do you want? S, M, L\n").title()
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry! please chose approprite size! ")
    exit
pepperoni = input("DO you want pepperoni? Y/N \n").title()
if pepperoni == "Y":
    bill += 2
elif pepperoni == "N":
    bill == bill
else:
    print("Sorry! please chose yes or no ")
extra_cheese = input("Do you want extra cheese? Y/N").title()
if extra_cheese == "Y":
    bill += 1
elif extra_cheese == "N":
    bill == bill 
else:
    print("Sorry! please chose yes ir no.")























# derived formate 

# bill = 0
# size = input("What size do you want? S, M, L: \n").title()
# if size == "S":
#     bill += 15
#     pepperoni = input("Do you wan pepperoni on your pizza? Y or N\n").title()
#     if pepperoni == "Y":
#         bill += 2
#         extra_cheese = input("Do you want extra cheese? Y or N").title()
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"You have to pay $ {bill}")
#         else:
#             bill == bill
#             print(f"You have to pay $ {bill}")
#     else:
#         bill == bill
#         print(f"You have to pay $ {bill}")
        
# elif size == "M":
#     bill += 20
#     pepperoni = input("Do you wan pepperoni on your pizza? Y or N\n").title()
#     if pepperoni == "Y":
#         bill += 2
#         extra_cheese = input("Do you want extra cheese? Y or N").title()
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"You have to pay $ {bill}")
#         else:
#             bill == bill
#             print(f"You have to pay $ {bill}")
#     else:
#         bill == bill
#         print(f"You have to pay $ {bill}")
        
        
# elif size == "L":
#     bill += 25
#     pepperoni = input("Do you wan pepperoni on your pizza? Y or N\n").title()
#     if pepperoni == "Y":
#         bill += 2
#         extra_cheese = input("Do you want extra cheese? Y or N").title()
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"You have to pay $ {bill}")
#         else:
#             bill == bill
#             print(f"You have to pay $ {bill}")
#     else:
#         bill == bill
#         print(f"You have to pay $ {bill}")
# else:
#     print("Choose the appropriate size! S,M,L")
