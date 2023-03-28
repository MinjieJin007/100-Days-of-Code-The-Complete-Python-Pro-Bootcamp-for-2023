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

earned_money = 0


def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# My original answer. It is right but too complicated
# def check_resources(rest_resources, wish):
#     """Return False when order cannot be made"""
#     if rest_resources["water"] < MENU[wish]["ingredients"]["water"]:
#         print("Sorry there is not enough water.")
#         return False
#     if wish != "espresso":
#         if rest_resources["milk"] < MENU[wish]["ingredients"]["milk"]:
#             print("Sorry there is not enough milk.")
#             return False
#     if rest_resources["coffee"] < MENU[wish]["ingredients"]["coffee"]:
#         print("Sorry there is not enough coffee.")
#         return False
#     return True


def check_money(drink):
    """Return True when the payment is accepted, or False if money
    is insufficient. Add accepted money to earned_money"""
    global earned_money
    print("Please insert coins.")
    quarters = int(input ("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    change_back = money - drink["cost"]
    change_back = round(change_back, 2)
    if money < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(change_back, 2)} in change.")
        earned_money += money
        return True


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    # include the situation of espresso, which don't use milk
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy!")


def coffee_machine():
    stop = False
    global earned_money
    while not stop:
        # Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        wish = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # Turn off the Coffee Machine by entering “ off ” to the prompt.
        if wish == "off":
            stop = True
        # When the user enters “report” to the prompt, a report
        # should be generated that shows the current resource values.
        elif wish == "report":
            earned_money = round(earned_money, 2)
            print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g "
                  f"\nMoney: ${earned_money}")
        else:
            drink = MENU[wish]
            if check_resources(drink["ingredients"]):
                if check_money(drink):
                    make_coffee(wish, drink["ingredients"])


coffee_machine()













