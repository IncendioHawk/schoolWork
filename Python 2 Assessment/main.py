def getDistance():
    distance = float(input("Enter the distance in kilometres: "))
    if distance > 0:
        return distance
    print("The distance must be greater than 0")
    return getDistance()

def getPassengers():
    return int(input("Enter the number of passengers: ")) 

def calculateFare(distance, passengers):
    fare = 2 * passengers + 1.5 * distance
    return fare

def round(number, dp):
    return int(number * (10 ** dp)) / (10 ** dp)

def main():
    distance = getDistance()
    passengers = getPassengers()
    fare = calculateFare(distance, passengers)
    fare = round(fare, 2)
    print(f"The fare is £{fare}")

main()