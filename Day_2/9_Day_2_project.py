bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
people = int(input("How many people are split the bill?\n"))
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
amount_per_person = total_bill / people
print(amount_per_person)