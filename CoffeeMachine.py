from enum import Enum


class Espresso(Enum):
    water = 250
    milk = 0
    coffee = 16
    price = 4


class Latte(Enum):
    water = 350
    milk = 75
    coffee = 20
    price = 7


class Cappuccino(Enum):
    water = 200
    milk = 100
    coffee = 12
    price = 6


class CoffeeMachine(object):
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def print_state(self):
        print('The coffee machine has:')
        print('{} of water'.format(self.water))
        print('{} of milk'.format(self.milk))
        print('{} of coffee beans'.format(self.coffee))
        print('{} of disposable cups'.format(self.cups))
        print('{} of money'.format(self.money))

    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            print()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.print_state()
            elif action == 'exit':
                break
            print()

    def check_resources(self, coffee_type):
        if self.water - coffee_type.water.value < 0:
            return False, coffee_type.water.name
        if self.milk - coffee_type.milk.value < 0:
            return False, coffee_type.milk.name
        if self.coffee - coffee_type.coffee.value < 0:
            return False, coffee_type.coffee.name
        if self.cups - 1 < 0:
            return False, coffee_type.coffee.name
        return True, None

    def make_coffee(self, coffee_type):
        enough_resources, missing_resource = self.check_resources(coffee_type)
        if enough_resources:
            print('I have enough resources, making you a coffee!')
        else:
            print('Sorry, not enough {}!'.format(missing_resource))
            return None

        self.water -= coffee_type.water.value
        self.milk -= coffee_type.milk.value
        self.coffee -= coffee_type.coffee.value
        self.cups -= 1
        self.money += coffee_type.price.value

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee = input()
        if coffee == '1':
            self.make_coffee(Espresso)
        elif coffee == '2':
            self.make_coffee(Latte)
        elif coffee == '3':
            self.make_coffee(Cappuccino)

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0


def main():
    coffee_machine_bratislava = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine_bratislava.action()


if __name__ == "__main__":
    main()
