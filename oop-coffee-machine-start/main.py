from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker
money_machine = MoneyMachine()
menu = Menu()

drink = input(f"What would you like? Your choices are {menu.get_items()}:")
print(f"That drink costs {menu.find_drink(drink).cost}")

print("Checking resources...")
#coffee_maker.report()
print(coffee_maker.is_resource_sufficient(drink))





money_machine.report()