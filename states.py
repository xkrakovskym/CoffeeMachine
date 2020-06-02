from abc import ABC, abstractmethod
from definitions import MachineState, CoffeeType


class State(ABC):

    def __init__(self):
        self.menu = None

    def __str__(self):
        return self.menu

    @abstractmethod
    def move_on(self, user_input, coffee_machine):
        pass


class MainMenu(State):

    def __init__(self):
        self.menu = MachineState.mainMenu.value

    def move_on(self, user_input, coffee_machine):
        if user_input == 'buy':
            return BuyMenu()
        elif user_input == 'fill':
            return FillWaterMenu()
        elif user_input == 'remaining':
            return RemainingMenu(coffee_machine)
        elif user_input == 'take':
            return TakeMenu(coffee_machine)
        elif user_input == 'exit':
            return ExitMenu(coffee_machine)
        else:
            return MainMenu()


class BuyMenu(State):

    def __init__(self):
        self.menu = MachineState.buyMenu.value

    def move_on(self, user_input, coffee_machine):
        return CoffeeMenu(user_input, coffee_machine)


class CoffeeMenu(State):

    def __init__(self, user_input, coffee_machine):
        try:
            coffee_done, missing_ingredient = coffee_machine.make_coffee(CoffeeType.type.value[user_input])

            if coffee_done:
                self.menu = MachineState.coffeeDone.value
            else:
                self.menu = MachineState.coffeeNotDone.value.format(missing_ingredient)
        except KeyError:
            self.menu = ''

    def move_on(self, user_input=None, coffee_machine=None):
        return MainMenu()


class FillWaterMenu(State):

    def __init__(self):
        self.menu = MachineState.fillWater.value

    def move_on(self, user_input, coffee_machine):
        try:
            user_input = int(user_input)
            coffee_machine.fill('water', user_input)
            return FillMilkMenu()
        except ValueError:
            return FillWaterMenu()


class FillMilkMenu(State):

    def __init__(self):
        self.menu = MachineState.fillMilk.value

    def move_on(self, user_input, coffee_machine):
        try:
            user_input = int(user_input)
            coffee_machine.fill('milk', user_input)
            return FillCoffeeMenu()
        except ValueError:
            return FillMilkMenu()


class FillCoffeeMenu(State):

    def __init__(self):
        self.menu = MachineState.fillCoffee.value

    def move_on(self, user_input, coffee_machine):
        try:
            user_input = int(user_input)
            coffee_machine.fill('coffee', user_input)
            return FillCupsMenu()
        except ValueError:
            return FillCoffeeMenu()


class FillCupsMenu(State):

    def __init__(self):
        self.menu = MachineState.fillCups.value

    def move_on(self, user_input, coffee_machine):
        try:
            user_input = int(user_input)
            coffee_machine.fill('cups', user_input)
            return MainMenu()
        except ValueError:
            return FillCupsMenu()


class RemainingMenu(State):

    def __init__(self, coffee_machine):
        contents = list(coffee_machine.contents)
        self.menu = MachineState.remainingMenu.value.format(amounts=contents)

    def move_on(self, user_input, coffee_machine):
        return MainMenu()


class TakeMenu(State):

    def __init__(self, coffee_machine):
        self.menu = MachineState.takeMenu.value.format(coffee_machine.take())

    def move_on(self, user_input, coffee_machine):
        return MainMenu()


class ExitMenu(State):

    def __init__(self, coffee_machine):
        self.menu = MachineState.exitState.value
        coffee_machine.stop()

    def move_on(self, user_input, coffee_machine):
        return None
