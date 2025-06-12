from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
CoffeeMaker = CoffeeMaker()
CoffeMachine = True

MoneyMachine =MoneyMachine()

menu = Menu()
while CoffeMachine is True:
    options = menu.get_items()
    choice = input(f"What woould you like? ({options}): ")
    if choice =="off":
        CoffeMachine = False
    elif choice=="report":
        MoneyMachine.report()
        CoffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(drink):
            if MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)

        

        
