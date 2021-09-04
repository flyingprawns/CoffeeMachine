from data import MENU
from data import resources


def print_report():
    print("-------------")
    print("status report")
    print("-------------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${resources['money']}")
    print()
    return


def in_menu(item_name):
    return item_name in MENU.keys()


def sufficient_resources(item_name):
    item_ingredients = MENU[item_name]["ingredients"]
    if resources["water"] < item_ingredients["water"]:
        print("Not enough water.")
        return False
    if resources["milk"] < item_ingredients["milk"]:
        print("Not enough milk.")
        return False
    if resources["coffee"] < item_ingredients["coffee"]:
        print("Not enough coffee.")
        return False
    return True


def print_cost(item_name):
    cost = MENU[item_name]['cost']
    print(f"Thanks for your order! Your item will cost ${cost}")
    return


def get_payment():
    total = 0.00
    quarters = int(input("Insert quarters (type the amount): "))
    total += quarters * 0.25
    dimes = int(input("Insert dimes (type the amount): "))
    total += dimes * 0.10
    nickels = int(input("Insert nickels (type the amount): "))
    total += nickels * 0.05
    pennies = int(input("Insert pennies (type the amount): "))
    total += pennies * 0.01
    return total


def make_coffee(item_name):
    item_ingredients = MENU[item_name]['ingredients']
    resources['water'] -= item_ingredients['water']
    resources['milk'] -= item_ingredients['milk']
    resources['coffee'] -= item_ingredients['coffee']
    print(f"Here is your {item_name}! Enjoy!!")
    return


while True:
    # Get user request
    user_request = input("\nEspresso, Latte, or Cappuccino? ('off' to turn off machine): ").lower()

    if user_request == "off":
        print("Shutting down vending machine.")
        break

    if user_request == "report":
        print_report()
        continue

    if not in_menu(user_request):
        print("This item is not in the menu. Please try again!\n")
        continue

    if not sufficient_resources(user_request):
        print("Type 'report' to see what the machine contains.\n")
        continue

    # Get payment from user
    print_cost(user_request)
    user_payment = get_payment()

    # Didn't pay enough!
    item_cost = MENU[user_request]['cost']
    if user_payment < item_cost:
        print("That's not enough money :( Refunding payment.")
        input()
        continue

    # User paid enough money. Keep the profit, offer change, make the coffee.
    else:
        resources['money'] += item_cost
        change = round(user_payment - item_cost, 2)
        print(f"Here is ${change} in change.")
        input()
        make_coffee(user_request)

