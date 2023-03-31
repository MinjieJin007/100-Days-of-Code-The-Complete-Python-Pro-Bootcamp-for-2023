from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        ordered_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink.cost):
            coffee_maker.make_coffee(ordered_drink)

