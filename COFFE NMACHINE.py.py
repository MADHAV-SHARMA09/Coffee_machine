print("""  
   _____ ____  ______ ______ ______ ______    __  __          _____ _    _ _____ _   _ ______ 
  / ____/ __ \|  ____|  ____|  ____|  ____|  |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
 | |   | |  | | |__  | |__  | |__  | |__     | \  / |  /  \ | |    | |__| | | | |  \| | |__   
 | |   | |  | |  __| |  __| |  __| |  __|    | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
 | |___| |__| | |    | |    | |____| |____   | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
  \_____\____/|_|    |_|    |______|______|  |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|
  """)

from gtts import gTTS
import playsound
import prettytable

rules = """WELCOME TO COFFEE MACHINE PLEASE CHOOSE AMONG THE FOLLOWING"""


def speech():
    tts = gTTS(text=rules, lang="en")
    filename = "rules.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speech()


def speak():
    tts = gTTS(text="thank you for purchasing the coffee", lang="en")
    filename = "bro.mp3"
    tts.save(filename)
    playsound.playsound(filename)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 120,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 110,
    }
}

# MENU={"NAME":{"INGREDIENT"{_____}}, "COST":___ }

situation = True  # for while loop

total_milk = 200
total_water = 500
coffee_beans = 50
money = 0

cost_espresso = MENU["espresso"]["cost"]
cost_latte = MENU["latte"]["cost"]
cost_cappuccino = MENU["cappuccino"]["cost"]


def coffee(n):
    global total_milk
    global total_water
    global coffee_beans
    global situation

    water_for_coffee = MENU[n]["ingredients"]["water"]
    total_water -= water_for_coffee

    milk_for_coffee = MENU[n]["ingredients"]["milk"]
    total_milk -= milk_for_coffee

    coffee_beans -= MENU[n]["ingredients"]["coffee"]

    

def cost(cost_for_coffee):
    global money
    global situation

    rupee_10 = int(input("no. of 10 rupee notes: "))
    rupee_50 = int(input("no. of 50 rupee notes: "))
    rupee_100 = int(input("no. of 100 rupee notes: "))

    total_money_entered = (rupee_10 * 10) + (rupee_50 * 50) + (rupee_100 * 100)

    if cost_for_coffee > total_money_entered:
        print("not enough money has been entered")
        print("money entered will be returned")
        situation = False

    elif cost_for_coffee == total_money_entered:
        print("money has been deposited")
        money += cost_for_coffee

    elif cost_for_coffee < total_money_entered:
        k = total_money_entered - cost_for_coffee
        print("money has been deposited")
        print(f"here's your change of rupees {k}")
        money += cost_for_coffee


while situation:
    print("""press
        1 to see resources
        2 to see menu
        3 for espresso
        4 for latte
        5 for cappuccino
        6 to see the amount of money the machine currently possesses""")

    choice = input("enter: ")

    if choice == "1":
        table = prettytable.PrettyTable()
        table.add_column("SNO.", [1, 2, 3, ])
        table.add_column("INGREDIENTS", ["MILK", "WATER", "COFFEE", ])
        table.add_column("AMOUNT", [f"{total_milk} ml", f"{total_water} ml", f"{coffee_beans} gm", ])

        table.align = "l"
        print(table)

    elif choice == "2":
        table = prettytable.PrettyTable()
        table.add_column("MENU", ["ESPRESSO", "LATTE", "CAPPUCCINO"])
        table.add_column("COST", ["100", "120", "110"])

        print(table)

    elif choice == "3":
        n = "espresso"
        print(f"cost for espresso is {cost_espresso}")
        cost(cost_espresso)
        coffee(n)
        if situation:
            print("your order will be ready in a minute")
            print("🅣🅗🅐🅝🅚 🅨🅞🅤 🅕🅞🅡 🅟🅤🅡🅒🅗🅐🅢🅔")
            speak()

    elif choice == "4":
        n = "latte"
        print(f"cost for latte is {cost_latte}")
        cost(cost_latte)
        coffee(n)
        if situation:
            print("your order will be ready in a minute")
            print("🅣🅗🅐🅝🅚 🅨🅞🅤 🅕🅞🅡 🅟🅤🅡🅒🅗🅐🅢🅔")
            speak()

    elif choice == "5":
        n = "cappuccino"
        print(f"cost for cappuccino is {cost_cappuccino}")
        cost(cost_cappuccino)
        coffee(n)
        if situation:
            print("your order will be ready in a minute")
            print("🅣🅗🅐🅝🅚 🅨🅞🅤 🅕🅞🅡 🅟🅤🅡🅒🅗🅐🅢🅔")
            speak()

    elif choice == "6":
        table = prettytable.PrettyTable()
        table.add_column("MONEY IN SYSTEM", [money])

        print(table)

    else:
        print("invalid input")
        break