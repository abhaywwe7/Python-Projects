import random

dice_value = [1,2,3,4,5,6]
roll = "yes"

while roll == "yes" or roll == "y" or roll == "YES":
    print("Rolling the dice........")
    print("The value is: ")
    print(random.choice(dice_value))
    roll = input("Wanna roll again?\n")

