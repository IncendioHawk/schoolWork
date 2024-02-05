import random
# List of treats
treats = ["Chocolate cake", "Fruit salad", "Ice cream", "Cookies", "Yogurt"]

# Assume the user has eaten all their vegetables (you can modify this condition)
hasEatenVegetables = input("Have you eaten all your vegtables? (yes/no):").lower() == "yes"

if hasEatenVegetables:
    chosenTreat = random.choice(treats)
    print(f"Congratulations! You've earned a {chosenTreat} for dessert.")
    eatTreat = input("Would you like to eat this one? (yes/no):").lower() == "yes"
    if eatTreat:
      print(f"Great! Enjoy your {chosenTreat}.")
    else:
      while True:
        treat = input("What treat would you like instead?:")
        if treat not in treats:
          print("Sorry, that's not an option.")
        else:
          print(f"Great! Enjoy your {treat}.")
          break
else:
    print("Remember to eat your vegetables first!")