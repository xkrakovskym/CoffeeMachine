from enum import Enum


class CoffeeType(Enum):
    Espresso = {'water': 250, 'milk': 0, 'coffee': 16, 'price': 4}
    Latte = {'water': 350, 'milk': 75, 'coffee': 20, 'price': 7}
    Cappuccino = {'water': 200, 'milk': 100, 'coffee': 12, 'price': 6}


class MachineState(Enum):
    mainMenu = 'Write action (buy, fill, take, remaining, exit):'
    buyMenu = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'
    fillWater = 'Write how many ml of water do you want to add:'
    fillMilk = 'Write how many ml of milk do you want to add:'
    fillCoffee = 'Write how many grams of coffee beans do you want to add:'
    fillCups = 'Write how many disposable cups of coffee do you want to add:'
    exitState = 'You are more than welcome next time!'

    def __str__(self):
        return self._state.name


class CoffeeMachine(object):

    def __init__(self, water, milk, coffee, cups, money):
        self._contents = {'water': water, 'milk': milk, 'coffee': coffee, 'cups': cups, 'money': money}
        self._state = MachineState(MachineState.mainMenu)

    def __str__(self):
        print_list = list(self._contents.values())
        return """The coffee machine has:
                {amounts[0]} of water
                {amounts[1]} of milk
                {amounts[2]} of coffee
                {amounts[3]} of disposable cups
                {amounts[4]} of money""".format(amounts=print_list)

    def __repr__(self):
        return self._contents

    def process_input(self):
        pass

    def is_running(self):
        if self._state == MachineState.exitState:
            return False
        else:
            print(self._state.value)
            return True

    def action(self, user_input=None):
        if self._state == MachineState.mainMenu:
            if user_input == 'buy':
                self._state = MachineState.buyMenu
                return self.is_running()
            elif user_input == 'fill':
                self._state = MachineState.fillWater
                return self.is_running()
            elif user_input == 'remaining':
                print(self)
                return self.is_running()
            elif user_input == 'take':
                print(self.take())
                return self.is_running()
            elif user_input == 'exit':
                self._state = MachineState.exitState
                return self.is_running()
            return self.is_running()

        elif self._state == MachineState.buyMenu:
            self.buy(user_input)
            self._state = MachineState.mainMenu

        elif self._state == MachineState.fillWater:
            self.fill('water', user_input)
            self._state = MachineState.fillMilk

        elif self._state == MachineState.fillMilk:
            self.fill('milk', user_input)
            self._state = MachineState.fillCoffee

        elif self._state == MachineState.fillCoffee:
            self.fill('coffee', user_input)
            self._state = MachineState.fillCups

        elif self._state == MachineState.fillCups:
            self.fill('cups', user_input)
            self._state = MachineState.mainMenu
        return self.is_running()

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
            self._state = MachineState.mainMenu
        else:
            print('Sorry, not enough {}!'.format(missing_resource))
            self._state = MachineState.mainMenu
            return None

        self._contents['water'] -= coffee_type.value['water']
        self._contents['milk'] -= coffee_type.value['milk']
        self._contents['coffee'] -= coffee_type.value['coffee']
        self._contents['cups'] -= 1
        self._contents['money'] += coffee_type.value['price']

    def buy(self, user_input):
        if user_input == '1':
            self.make_coffee(CoffeeType.Espresso)
        elif user_input == '2':
            self.make_coffee(CoffeeType.Latte)
        elif user_input == '3':
            self.make_coffee(CoffeeType.Cappuccino)

    def fill(self, content_type, user_input):
        self._contents[content_type] += int(user_input)

    def take(self):
        self._contents['money'] = 0
        return'I gave you ${}'.format(self._contents['money'])


class InputProcessor:
    pass


def main():
    coffee_machine_bratislava = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine_bratislava.action()

    while True:
        user_input = input()
        is_running = coffee_machine_bratislava.action(user_input)
        if not is_running:
            break


if __name__ == "__main__":
    main()
