import random
friends = ["Alice", "bob","Charlie","David","Emanuel"]
computer = random.choice(friends) # This is  the fist option 
print(computer)

print(friends[random.randint(0,4)]) # This will be the scond way, 
# Note:- here if we don't use the square bracket then if will print only the no bwt 0 to 1, if we use the bracket and before the bracket we have to use the variable name.Like here is the "Friends".
