from enum import Enum


class CoffeeType(Enum):
    Espresso = {'water': 250, 'milk': 0, 'coffee': 16, 'price': 4}
    Latte = {'water': 350, 'milk': 75, 'coffee': 20, 'price': 7}
    Cappuccino = {'water': 200, 'milk': 100, 'coffee': 12, 'price': 6}


class MachineState(Enum):
    mainMenu = 1
    buyMenu = 2
    fillWater = 3
    fillMilk = 4
    fillCoffee = 5
    fillCups = 6
    exitState = 7

    def __str__(self):
        return self._state.name


class CoffeeMachine(object):

    def __init__(self, water, milk, coffee, cups, money):
        self._contents = {'water': 200, 'milk': 100, 'coffee': 12, 'cups': 9, 'money': 500}
        self._state = MachineState(MachineState.buyMenu)

    def __str__(self):
        print_list = list(self._contents.values())
        return """The coffee machine has:
                {amounts[0]} of water
                {amounts[1]} of milk
                {amounts[2]} of coffee
                {amounts[3]} of disposable cups
                {amounts[4]} of money""".format(amounts=print_list)

    def process_input(self):
        pass

    def is_running(self):
        if self._state == MachineState.exitState:
            return False
        else:
            return True

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
                print(self)
            elif action == 'exit':
                break
            print()

    def check_resources(self, coffee_type):
        if self._contents['water'] - coffee_type.value['water'] < 0:
            return False, 'water'
        if self._contents['milk'] - coffee_type.value['milk'] < 0:
            return False, 'milk'
        if self._contents['coffee'] - coffee_type.value['coffee'] < 0:
            return False, 'coffee'
        if self._contents['cups'] - 1 < 0:
            return False, 'cups'
        return True, None

    def make_coffee(self, coffee_type):
        enough_resources, missing_resource = self.check_resources(coffee_type)
        if enough_resources:
            print('I have enough resources, making you a coffee!')
        else:
            print('Sorry, not enough {}!'.format(missing_resource))
            return None

        self._contents['water'] -= coffee_type.value['water']
        self._contents['milk'] -= coffee_type.value['milk']
        self._contents['coffee'] -= coffee_type.value['coffee']
        self._contents['cups'] -= 1
        self._contents['money'] += coffee_type.value['price']

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee = input()
        if coffee == '1':
            self.make_coffee(CoffeeType.Espresso)
        elif coffee == '2':
            self.make_coffee(CoffeeType.Latte)
        elif coffee == '3':
            self.make_coffee(CoffeeType.Cappuccino)

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self._contents['water'] += int(input())
        print('Write how many ml of milk do you want to add:')
        self._contents['milk'] += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self._contents['coffee'] += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self._contents['cups'] += int(input())

    def take(self):
        print('I gave you ${}'.format(self._contents['money']))
        self._contents['money'] = 0


def main():
    coffee_machine_bratislava = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine_bratislava.action()


if __name__ == "__main__":
    main()
