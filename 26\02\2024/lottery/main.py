def userInput():
   try:
        num: int = int(input("Please enter a number between 1 and 20: "))
    if num < 1 or num > 20:
        print("Invalid number")
        return userInput()
   except ValueError:
        print("Invalid input")
        return userInput()

def fullInput():
     nums: List[int] = []
     for i in range(5):
         nums.append(userInput())