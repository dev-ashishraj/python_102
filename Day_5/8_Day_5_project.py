
import random

# Lists of all possible characters to use in the password
# Note: Numbers are strings ('1') so they can be added to the password text
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*']

print("Welcome to the Password Generator!")

# Get user input for how many of each character type they want
nr_letter = int(input("How many alphabets do you want in your password? \n"))
nr_symbol = int(input("How many symbols do you want in your password?\n"))
nr_number = int(input("How many numbers do you want in your password?\n"))

# --- Easy Level: Password is built in a specific order (Letters + Symbols + Numbers) ---

# # Start with an empty string to store the password
# password = ""

# # Loop to pick random letters and add them to the password
# for char in range(0, nr_letter):
#     # random.choice picks one item from the 'letters' list
#     password += random.choice(letters)

# # Loop to pick random symbols and add them to the password
# for char in range(0, nr_symbol):
#     password += random.choice(symbols)

# # Loop to pick random numbers and add them to the password
# for char in range(0, nr_number):
#     password += random.choice(numbers)

# # Print the final generated password
# print(f"Your password is: {password}")


# --- Hard Level Logic ---

# 1. Create an empty list to store the characters
# We use a List [] instead of a String "" because lists can be shuffled
password_list = []

# 2. Add random letters to the list
for char in range(0, nr_letter):
    password_list.append(random.choice(letters))

# 3. Add random numbers to the list
for char in range(0, nr_number):
    password_list.append(random.choice(numbers))

# 4. Add random symbols to the list
for char in range(0, nr_symbol):
    password_list.append(random.choice(symbols))

# 5. The "Hard" part: Randomly reorder the items in the list
# This mixes the letters, numbers, and symbols together
random.shuffle(password_list)

# 6. Convert the list back into a string
# We start with an empty string and loop through the list to add each character
final_password = ""
for char in password_list:
    final_password += char

# 7. Print the final result
print(f"Your shuffled password is: {final_password}")
