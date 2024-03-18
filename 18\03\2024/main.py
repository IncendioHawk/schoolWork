price = float(input("Enter the price of your item: "))
discountRate = float(input("Enter the discount rate: "))
discount = price * discountRate / 100
discountedPrice = price - discount
print(f"Price before discount = £{price}")
print(f"Discount rate = {discountRate}%")
print(f"Discount = {discount}%")
print(f"Price after discount = {discountedPrice}%")