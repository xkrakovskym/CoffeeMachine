from enum import Enum


class MachineState(Enum):
    mainMenu = 'Write action (buy, fill, take, remaining, exit):'
    buyMenu = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'
    coffeeDone = 'I have enough resources, making you a coffee!\n'
    coffeeNotDone = 'Sorry, not enough {}!\n'
    fillWater = 'Write how many ml of water do you want to add:'
    fillMilk = 'Write how many ml of milk do you want to add:'
    fillCoffee = 'Write how many grams of coffee beans do you want to add:'
    fillCups = 'Write how many disposable cups of coffee do you want to add:'
    remainingMenu = """The coffee machine has:
                        {amounts[0]} of water
                        {amounts[1]} of milk
                        {amounts[2]} of coffee
                        {amounts[3]} of disposable cups
                        {amounts[4]} of money\n"""
    takeMenu = 'I gave you ${}\n'
    exitState = 'You are more than welcome next time!'


class CoffeeType(Enum):
    type = {'1': {'water': 250, 'milk': 0, 'coffee': 16, 'price': 4},       # espresso
            '2': {'water': 350, 'milk': 75, 'coffee': 20, 'price': 7},      # latte
            '3': {'water': 200, 'milk': 100, 'coffee': 12, 'price': 6}}     # cappuccino