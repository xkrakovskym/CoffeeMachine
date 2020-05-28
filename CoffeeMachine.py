from enum import Enum
import abc


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

    @abc.abstractmethod
    def move_on(self):
        return


class CoffeeMachine(object):

    def __init__(self, water, milk, coffee, cups, money):
        self._contents = {'water': water, 'milk': milk, 'coffee': coffee, 'cups': cups, 'money': money}
        self._state = MachineState(MachineState.mainMenu)

    def __str__(self):
        content_amounts = list(self._contents.values())
        return """The coffee machine has:
                {amounts[0]} of water
                {amounts[1]} of milk
                {amounts[2]} of coffee
                {amounts[3]} of disposable cups
                {amounts[4]} of money""".format(amounts=content_amounts)

    def __repr__(self):
        return self._contents

    def is_running(self):
        if self._state == MachineState.exitState:
            return False
        else:
            return True

    def action(self, user_input=None):
        if self._state == MachineState.mainMenu:
            if user_input == 'buy':
                self._state = MachineState.buyMenu
            elif user_input == 'fill':
                self._state = MachineState.fillWater
            elif user_input == 'remaining':
                return self.__str__() + '\n' + self._state.mainMenu.value
            elif user_input == 'take':
                return self.take() + '\n' + self._state.mainMenu.value
            elif user_input == 'exit':
                self._state = MachineState.exitState

            return self._state.value

        elif self._state == MachineState.buyMenu:
            self._state = MachineState.mainMenu
            return self.buy(user_input) + '\n' + self._state.mainMenu.value

        elif self._state == MachineState.fillWater:
            self.fill('water', user_input)
            self._state = MachineState.fillMilk
            return self._state.value

        elif self._state == MachineState.fillMilk:
            self.fill('milk', user_input)
            self._state = MachineState.fillCoffee
            return self._state.value

        elif self._state == MachineState.fillCoffee:
            self.fill('coffee', user_input)
            self._state = MachineState.fillCups
            return self._state.value

        elif self._state == MachineState.fillCups:
            self.fill('cups', user_input)
            self._state = MachineState.mainMenu
            return self._state.value

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
            output = 'I have enough resources, making you a coffee!'
        else:
            output = 'Sorry, not enough {}!'.format(missing_resource)

        self._contents['water'] -= coffee_type.value['water']
        self._contents['milk'] -= coffee_type.value['milk']
        self._contents['coffee'] -= coffee_type.value['coffee']
        self._contents['cups'] -= 1
        self._contents['money'] += coffee_type.value['price']

        return output

    def buy(self, user_input):
        if user_input == '1':
            return self.make_coffee(CoffeeType.Espresso)
        elif user_input == '2':
            return self.make_coffee(CoffeeType.Latte)
        elif user_input == '3':
            return self.make_coffee(CoffeeType.Cappuccino)

    def fill(self, content_type, user_input):
        self._contents[content_type] += int(user_input)

    def take(self):
        output = 'I gave you ${}'.format(self._contents['money'])
        self._contents['money'] = 0
        return output


class InputProcessor(object):

    def print_to_user(self, output):
        print(output)

    # input also here


def main():
    coffee_machine_bratislava = CoffeeMachine(400, 540, 120, 9, 550)
    machine_interface = InputProcessor()
    user_input = None

    while coffee_machine_bratislava.is_running():
        machine_interface.print_to_user(coffee_machine_bratislava.action(user_input))
        user_input = input()


if __name__ == "__main__":
    main()
