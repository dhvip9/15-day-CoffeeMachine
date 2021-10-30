from Tank_Menu import menu
from Tank_Menu import resource
from Tank_Menu import coffee_sold
import design


def tank(select_coffee):
    if select_coffee != "espresso":
        use_milk = menu[select_coffee]["milk"]
        resource["milk"] -= use_milk

    use_water = menu[select_coffee]["water"]
    use_coffee = menu[select_coffee]["coffee"]
    resource["water"] -= use_water
    resource["coffee"] -= use_coffee


def check_tank(selected_coffee):
    check = 0
    want_water = menu[selected_coffee]["water"]
    if want_water > resource["water"]:
        check += 1
        print("| Water | Is Out of Stock")

    if selected_coffee != "espresso":
        want_milk = menu[selected_coffee]["milk"]
        if want_milk > resource["milk"]:
            check += 1
            print("| Milk | Is Out of Stock")

    want_coffee = menu[selected_coffee]["coffee"]
    if want_coffee > resource["coffee"]:
        check += 1
        print("| Coffee | Is Out of Stock")

    if check > 0:
        return True


def payback(selected_coffee, total_pay):
    pay = total_pay - menu[selected_coffee]["cost"]
    print(pay)
    if pay > resource["money"]:
        print("\n [ Not Having Enough Change ]")
        return False
    else:
        coffee_sold[selected_coffee] += 1
        return pay


def units(item):
    if item == "water" or item == "milk":
        return "ml"
    elif item == "coffee":
        return "g"
    elif item == "money":
        return "$"
    else:
        return "cups"


def money_by_day(selected_coffee):
    print(f"Here is Your | {selected_coffee} | ☕. Enjoy it! ")
    resource["money"] += menu[selected_coffee]["cost"]


def report(final_resource, sold_coffee):
    print("[ Resource in Tank ]")
    for item in final_resource:
        units_item = units(item)
        print(f"{item}:  {final_resource[item]}{units_item}")
    print("\n[ Coffee are sold ]")
    for item in sold_coffee:
        units_item = units(item)
        print(f"{item}:  {sold_coffee[item]} {units_item}")
    print("--------------------------------------------\n")


def refill():
    resource["water"] = 300
    resource["milk"] = 200
    resource["coffee"] = 100
    resource["money"] = 5


print(design.logo())
Exit = False
while not Exit:
    while True:
        user_selection = input("What Would you Like ?\n[ | Espresso |, | Latte |, | Cappuccino | ]\n>> ").lower()
        if user_selection == "exit":
            Exit = True
            break
        elif user_selection == "report/d":
            report(resource, coffee_sold)
            break
        elif user_selection == "refill/d":
            refill()
            print("refilling is Successful")
            print("--------------------------------------------\n")
            break


        print("[ Please Insert Coins ]")
        if check_tank(user_selection):
            print("--------------------------------------------\n")
            break
        quarter = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many Dimes?:    ")) * 0.10
        nickles = int(input("how many Nickles?:  ")) * 0.05
        penny = int(input("how many pennies?:  ")) * 0.01

        user_total_amt = quarter + dimes + nickles + penny
        change = payback(user_selection, user_total_amt)
        if change < 0:
            print(f"Sorry that's not enough money.\n[ Money Refunded | {user_total_amt}]")

        round_change = round(change, 2)
        print(f"\n[ Here is | ${round_change} | in change. ]")

        money_by_day(user_selection)
        tank(user_selection)
        print("--------------------------------------------\n")
