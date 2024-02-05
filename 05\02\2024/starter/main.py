def remainderBy5(n):
    return n % 5

def isOdd(n):
    return n % 2

def perfectGroups(n):
    return False if isOdd(n) else False if isOdd(n / 2) else True

def main():
    numOfPeople = int(input("Enter the number of people: "))
    if (perfectGroups(numOfPeople)):
        print("Perfect groups of 4")
    else:
        print("You will be split up")
main()