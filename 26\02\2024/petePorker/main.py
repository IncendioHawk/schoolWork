STOCK = [
    {
        'name': 'scotch eggs',
        'price': 0.45,
    }, {
        'name': 'pork pies',
        'price': 0.85,
    }, {
        'name': 'quiche tarts',
        'price': 1.49,
    }
]

def validateOrder(num:int) -> bool:
    return num <= 20 and num >= 1

def takeItemOrder(item:str) -> int:
    try:
        num: int = int(input(f'Enter the number of {item} to buy: '))
        if not validateOrder(num):
            print('Please enter a number between 1 and 20.\n')
            return takeItemOrder(item)
    except ValueError:
        print('Please enter a valid number.\n')
        return takeItemOrder(item)
    return num

def takeFullOrder() -> []:
    order = []
    for item in STOCK:
        num: int = takeItemOrder(item['name'])
        order.append({
            'name': item['name'],
            'quantity': num,
            'price': item['price'] * num
        })
    print(f'----\nYou selected {order[0]["quantity"]} Scotch eggs, {order[1]["quantity"]} pork pies and {order[2]["quantity"]} quiche tarts.\n----\n')
    happy: str = input('Are you happy with this selection? (y/n): ').lower() == 'y'
    if happy:
        print('Excellent! Here is your receipt: \n\n')
        return order
    return takeFullOrder()

def main():
    print('--- Welcome to Pete Porker\'s Pork Pie Emporium ---\nScotch eggs are 45p, pork pies are 85p and quiche tarts are £1.49.\n')
    order = takeFullOrder()
    for item in order:
        print(f'{item["quantity"]} {item["name"]} = £{item["price"]:.2f}')
    print('-----')
    print(f'Total: £{sum([item["price"] for item in order]):.2f}')


main()