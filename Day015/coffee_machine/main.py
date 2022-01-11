# OUR COFFEE MACHINE MAKES 3 FLAVORS
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0.0
}
is_on: bool = True
user_money: float = 0.0
user_choice: str


def show_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    profit = resources['profit']
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit:.2f}')


def check_resources(ingredients: dict) -> bool:
    is_sufficient = True
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return is_sufficient


def get_payment() -> float:
    print('Please insert coins')
    quarters = int(input('\tQuarters: ')) * 0.25
    dimes = int(input('\tDimes: ')) * 0.10
    nickels = int(input('\tNickels: ')) * 0.05
    pennies = int(input('\tPennies: ')) * 0.01
    return quarters + dimes + nickels + pennies


def check_user_funds(choice: dict) -> int:
    cost: float = choice['cost']
    return -1 if user_money < cost else 1 if user_money > cost else 0


def make_coffee(drink_name: str, ingredients: dict):
    resources['water'] -= ingredients['water']
    resources['coffee'] -= ingredients['coffee']
    if drink_name == 'latte' or drink_name == 'cappuccino':
        resources['milk'] -= ingredients['milk']


while is_on:
    user_choice = input('What would you like? (espresso/latte/cappuccino):\n').lower()

    if user_choice == "off":
        is_on = False
        break

    if user_choice == 'report':
        show_report()

    elif user_choice in ['espresso', 'latte', 'cappuccino']:
        drink: dict = MENU[user_choice]

        # FIRST, make sure the machine has sufficient resources to make the coffee drink
        sufficient_resources = check_resources(drink['ingredients'])
        if not sufficient_resources:
            break

        # SECOND, prompt the user to insert coins
        user_money += get_payment()

        # THIRD, check that the user has inserted enough money
        if check_user_funds(drink) == -1:
            print("Sorry that's not enough money. Money refunded.")
            user_money = 0.0
            break
        elif check_user_funds(drink) == 1:
            refund = user_money - drink['cost']
            user_money -= refund
            print(f"Here is ${refund:.2f} in change.")
        resources['profit'] += user_money

        # FOURTH, make the chosen drink
        make_coffee(user_choice, drink['ingredients'])

        # LAST, present the user with the drink.
        print(f'Here is your {user_choice} ☕️. Enjoy!')
