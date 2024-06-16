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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many nickle? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    total += int(input("How many dimes? ")) * 0.1
    return total


def transaction_successful(amount_received, drink_cost):
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost,2)
        print(f"Here's your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")


machine_on = True
while machine_on:
    ask_user = input("What would you like? (espresso/latte/cappuccino): ")
    if ask_user == 'off':
        machine_on = False
    elif ask_user == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[ask_user]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment,drink['cost']):
                make_coffee(ask_user,drink['ingredients'])




