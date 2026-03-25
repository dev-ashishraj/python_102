taking_input = int(input("Which table you want to print?\n"))
table = 0 
for number in range(1,11):
    print(taking_input * table)
    table += 1
    # print(taking_input * table)