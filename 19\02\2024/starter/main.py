import random
holidayDests = ["Paris", "Barcelona", "New York", "Tokyo", "Sydney", "Rome"]

vowels = ["a", "e", "i", "o", "u"]
def randomVowel():
    return random.choice(vowels)

def checkUserInput(userInput):
    randVowel = randomVowel()
    if userInput == randVowel:
        return (f"Random vowel: {randVowel}\nThe vowels matched")
    else:
        return f"Random vowel: {randVowel}\nThe vowels didn't match"

def main():
    dest = random.choice(holidayDests)
    print(f"Why don't you go to {dest} on holiday?")
    userInput = input("Enter a vowel: ")
    print(checkUserInput(userInput))

main()