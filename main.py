MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
units  ={
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "Money" : "$" }

def inventory(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return  False
        return  True

def change():
    print("enter coins.")
    quarter = (int(input("how many quarters?: "))*0.25)
    dime = (int(input("how many dimes?: "))*0.10)
    nickels = (int(input("how many nickels?: "))*0.05)
    pennies = (int(input("how many pennies?: "))*0.01)
    total =  quarter+dime+nickels+pennies
    return  total

def payment(total , drink_cost):
    global profit
    if total >= drink_cost:
        profit += total
        due = round(total  - drink_cost,2)
        print(f'ohh we own your ${due}, here is it')
        return  True
    else:
        print("Sorry that's not enough money. Money refunded")
        return  False


def make_coffe (drinkName,orderIngredients):
    for item in orderIngredients:
        resources[item] -=orderIngredients[item]
    print(f"Here is your drink {drinkName} 😜, Enjoy!")

coffee_Machine = True
profit = 0
while coffee_Machine is True:
    coffe = (input("What would you like? (espresso/latte/cappuccino):").lower())
    if coffe == 'off':
        coffee_Machine = False
    elif coffe =="report":
        print(f'Water: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}ml')
        print(f'Money: ${profit}')
    else:
        Drink = MENU[coffe]
        if inventory(Drink['ingredients']):
            pay =change()
            payment(pay,Drink['cost'])
            make_coffe( coffe,Drink['ingredients'])




