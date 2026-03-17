import random
print("Welcome to Rock, paper, scissors")
user_input = input("What you want to choose? Rock, Paper, Scissor.\n").title()
game = ["Rock", "Paper", "Scissors"]
computer_chice = random.choice(game)

if user_input == "Rock" and computer_chice == "Paper":
    print(f" You lose!, Your choice {user_input} but computer choice {computer_chice}")
elif user_input == "Rock" and computer_chice == "Scissors":
    print(f"You won! Your choice {user_input} and computer choice {computer_chice}")
elif user_input == "Paper" and computer_chice == "Rock":
    print(f"You won! Your choice {user_input} and computer choice {computer_chice}")
elif user_input == "Scissors" and computer_chice == "Rock":
    print(f"You lose! Your choice {user_input} and computer choice {computer_chice}")
elif user_input == "Paper" and computer_chice == "Scissors":
    print(f"You lose! Your choice {user_input} and computer choice {computer_chice}")
elif user_input == "Scissors" and computer_chice == "Paper":
    print(f"You won!, Your choice {user_input} and computer choice {computer_chice}")
elif user_input == computer_chice:
    print(f"Match drow! Your choice {user_input} and computer choice {computer_chice}")
else:
    print("You lose!, You choose the wrong carecter.")
