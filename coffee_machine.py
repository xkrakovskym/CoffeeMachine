from states import MainMenu, TakeMenu, RemainingMenu, CoffeeMenu
from definitions import MachineState


class CoffeeMachine(object):

    def __init__(self, water, milk, coffee, cups, money):
        self._contents = {'water': water, 'milk': milk, 'coffee': coffee, 'cups': cups, 'money': money}
        self._is_running = True
        self._state = MainMenu()

    @property
    def contents(self):
        return self._contents.values()

    @property
    def state(self):
        return self._state

    def stop(self):
        self._is_running = False

    def is_running(self):
        return self._is_running

    def check_resources(self, coffee_type):
        if self._contents['water'] - coffee_type['water'] < 0:
            return False, 'water'
        if self._contents['milk'] - coffee_type['milk'] < 0:
            return False, 'milk'
        if self._contents['coffee'] - coffee_type['coffee'] < 0:
            return False, 'coffee'
        if self._contents['cups'] - 1 < 0:
            return False, 'cups'
        return True, None

    def make_coffee(self, coffee_type):
        enough_resources, missing_resource = self.check_resources(coffee_type)
        if enough_resources:
            self._contents['water'] -= coffee_type['water']
            self._contents['milk'] -= coffee_type['milk']
            self._contents['coffee'] -= coffee_type['coffee']
            self._contents['cups'] -= 1
            self._contents['money'] += coffee_type['price']

            return True, None
        else:
            return False, missing_resource

    def fill(self, content_type, amount):
        self._contents[content_type] += int(amount)

    def take(self):
        money_to_take = self._contents['money']
        self._contents['money'] = 0
        return money_to_take

    def action(self, user_input=None):
        self._state = self.state.move_on(user_input, self)
        return self._state


class InputProcessor(object):

    @staticmethod
    def print_to_user(output):
        print(output)

    @staticmethod
    def process_input(coffee_machine):
        if type(coffee_machine.state) in [TakeMenu, RemainingMenu, CoffeeMenu]:
            print(coffee_machine.action())

        print(coffee_machine.action(input()))


def main():
    coffee_machine_bratislava = CoffeeMachine(400, 540, 120, 9, 550)
    InputProcessor.print_to_user(coffee_machine_bratislava.state)
    while coffee_machine_bratislava.is_running():
        InputProcessor.process_input(coffee_machine_bratislava)


if __name__ == "__main__":
    main()
