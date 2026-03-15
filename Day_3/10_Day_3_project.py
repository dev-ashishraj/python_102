print("Welcome to treasure isand game\nYou have to find treassure!")
choice_1 = input('You\'re at a crossroad, where do you want to go? type "Left" or "Right". \n').title()
if choice_1 == "Left":
    choice_2 = input("There  is water in frount of you you want to take a 'boat' or 'swim'.\n ").title()
    if choice_2 == "Boat":
        choice_3 = input("there is 2 door\'s which one you want to go? 'red' or 'blue'.\n").title()
        if choice_3 == "Blue":
            print("You Won!, You get the treasure")
        elif choice_3 == "Red":
            print("You loss! In this door there are a poisonous snakes.")
        else:
            print("You lose! You didn't chose the apropriat door")
    elif choice_2 == "Swim":
        print("You lose! You have been eaten by a crocodile!")
        exit
    else:
        print("You lose! You have selected a wrong track")
        exit
elif choice_1 == "Right":
    print("You lose! In this road there is a loat of scorpions ")
    exit
else:
    print("You lose! You have taken a wrong parth.")










print("Welcome to Treasure Island! Your mission is to find the treasure.")

c1 = input('Crossroad: "Left" or "Right"? ').title()
if c1 == "Left":
    c2 = input('Water: "Boat" or "Swim"? ').title()
    if c2 == "Boat":
        c3 = input('Doors: "Red" or "Blue"? ').title()
        if c3 == "Blue":
            print("You Win! You found the treasure!")
        else:
            print("Game Over! " + ("Snakes!" if c3 == "Red" else "Wrong door."))
    else:
        print("Game Over! " + ("Eaten by crocodiles!" if c2 == "Swim" else "Wrong track."))
else:
    print("Game Over! " + ("Scorpions!" if c1 == "Right" else "Wrong path."))