class CoffeeMachine:
    def __init__(self):
        super(self)
        self.is_on: bool = True
        self.user_money: float = 0.0
        self.user_choice: str
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "profit": 0.0
        }

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

    def show_report(self):
        water = self.resources['water']
        milk = self.resources['milk']
        coffee = self.resources['coffee']
        profit = self.resources['profit']
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit:.2f}')

    def check_resources(self, ingredients: dict) -> bool:
        is_sufficient = True
        for item in ingredients:
            if ingredients[item] >= self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return is_sufficient

    def get_payment(self) -> float:
        print('Please insert coins')
        quarters = int(input('\tQuarters: ')) * 0.25
        dimes = int(input('\tDimes: ')) * 0.10
        nickels = int(input('\tNickels: ')) * 0.05
        pennies = int(input('\tPennies: ')) * 0.01
        return quarters + dimes + nickels + pennies

    def check_user_funds(self, choice: dict) -> int:
        cost: float = choice['cost']
        return -1 if self.user_money < cost else 1 if self.user_money > cost else 0

    def make_coffee(self, drink_name: str, ingredients: dict):
        self.resources['water'] -= ingredients['water']
        self.resources['coffee'] -= ingredients['coffee']
        if drink_name == 'latte' or drink_name == 'cappuccino':
            self.resources['milk'] -= ingredients['milk']

    def get_user_choice(self):
        while self.is_on:
            self.user_choice = input('What would you like? (espresso/latte/cappuccino):\n').lower()

            if self.user_choice == "off":
                self.is_on = False
                break

            if self.user_choice == 'report':
                self.show_report()

            elif self.user_choice in ['espresso', 'latte', 'cappuccino']:
                drink: dict = self.MENU[self.user_choice]

                # FIRST, make sure the machine has sufficient resources to make the coffee drink
                sufficient_resources = self.check_resources(drink['ingredients'])
                if not sufficient_resources:
                    break

                # SECOND, prompt the user to insert coins
                self.user_money += self.get_payment()

                # THIRD, check that the user has inserted enough money
                if self.check_user_funds(drink) == -1:
                    print("Sorry that's not enough money. Money refunded.")
                    user_money = 0.0
                    break
                elif self.check_user_funds(drink) == 1:
                    refund = self.user_money - drink['cost']
                    self.user_money -= refund
                    print(f"Here is ${refund:.2f} in change.")
                self.resources['profit'] += self.user_money

                # FOURTH, make the chosen drink
                self.make_coffee(self.user_choice, drink['ingredients'])

                # LAST, present the user with the drink.
                print(f'Here is your {self.user_choice} ☕️. Enjoy!')


coffee_machine = CoffeeMachine()
coffee_machine.get_user_choice()