from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
money = MoneyMachine()
items = Menu()


machine_on = True
while machine_on:
    options = items.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        coffee.report()
        money.report()
    else:
        drink = items.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)




