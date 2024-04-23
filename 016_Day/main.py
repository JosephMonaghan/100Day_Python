from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_moneymachine=MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    options=my_menu.get_items()
    user_order = input(f"What would you like? ({options})")
    if user_order == "off":
        coffee_machine_on = False
    elif user_order == "report":
        my_coffee_maker.report()
        my_moneymachine.report()
    else:
        drink=my_menu.find_drink(user_order)
        enough_resources = my_coffee_maker.is_resource_sufficient(drink)

        if enough_resources:
            payment_valid = my_moneymachine.make_payment(drink.cost)
            if payment_valid:
                my_coffee_maker.make_coffee(drink)

    

