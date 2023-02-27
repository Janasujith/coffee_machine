# TODO 1: MENU and RESOCURCE
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


# TODO 3: Resource and resource format
def resource(resources, water, milk, coffee, cost):
    if resources == 1:
        print(f'water:{water}ml\ncoffee:{coffee}ml\ncost:{cost}')
    else:
        print(f'water:{water}ml\nMilk:{milk}ml\ncoffee:{coffee}mg\ncost:{cost}')


# TODO 4: transcation for coffee machine

def transaction(x, res):
    print('please insert coin')
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    q = 0.25
    d = 0.10
    n = 0.05
    p = 0.01
    no_q = int(input(("No of quarter")))
    no_d = int(input("No of dimes"))
    no_n = int(input("No of  nickles"))
    no_p = int(input("No of pennies"))
    given_penny = (q * no_q) + (d * no_d) + (n * no_n) + (p * no_p)
    if given_penny < x['cost']:
        print("sorry that's not sufficident money. money refunded")
    else:
        change = round((given_penny - x['cost']), 2)
        print(f'Here is ${change} in change')
        print(f'here is your {res}! ☕ .enjoy!')







# TODO 2:Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
machine_status = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
cost = 0
resources = 0

while machine_status:
    user_prompt = input("what would you like?(espresso/latte/cappuccino)")
    if user_prompt == "espresso":
        res = list(MENU.keys())[0]
        x = MENU['espresso']
        y = x['cost']
        report_ingredients = x['ingredients']
        resources = 1
        cost += y
        report_water = report_ingredients['water']
        report_coffee = report_ingredients['coffee']
        water = water - report_water
        coffee = coffee - report_coffee
        milk = 0
        transaction(x, res)



    elif user_prompt == "latte":
        res = list(MENU.keys())[1]
        x = MENU['latte']
        y = x['cost']
        report_ingredients = x['ingredients']
        resources = 2
        cost += y
        report_water = report_ingredients['water']
        report_coffee = report_ingredients['coffee']
        report_milk = report_ingredients['milk']
        water = water - report_water
        coffee = coffee - report_coffee
        milk = milk - report_milk
        transaction(x, res)



    elif user_prompt == "cappuccino":
        res = list(MENU.keys())[2]
        x = MENU['cappuccino']
        y = x['cost']
        report_ingredients = x['ingredients']
        resources = 3
        cost += y
        report_water = report_ingredients['water']
        report_coffee = report_ingredients['coffee']
        report_milk = report_ingredients['milk']
        water = water - report_water
        coffee = coffee - report_coffee
        milk = milk - report_milk
        transaction( x, res)



    elif user_prompt == "off":
        print("the machine is off")
        machine_status = False

    elif user_prompt == "report":
            resource(resources=resources, water=water, milk=milk, coffee=coffee, cost=cost)

    else:
        print('enter the correct option')
