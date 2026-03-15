# BMI Calculator with Interpretations

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"


print("Welcome to BMI calculator!")
cm_or_m = input("In which matrick system do you have measure your height in cm or m\n").title()
if cm_or_m == "Cm":
    height = float(input("What is your height in Cm?\n"))
    weight = float(input("What is your weight in kg?\n"))
    height_cm = height / 100
    square = height_cm ** 2
    weight_in_kg = weight / square
    if weight_in_kg < 18.5:
        print(f"underweight")
    elif 18.5 > weight_in_kg < 25 :
        print(F"normal weight")
    else:
        print("overweight")
else: 
    height = float(input("What is your height in M?\n"))
    weight = float(input("What is your weight in kg?\n"))
    square = height ** 2
    weight_in_kg = weight / square
    if weight_in_kg < 18.5:
        print(f"underweight")
    elif 18.5 > weight_in_kg < 25 :
        print(F"normal weight")
    else:
        print("overweight")