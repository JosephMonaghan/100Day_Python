import os
os.system('Clear')

# TODO Import the database
from database import MENU, resources

resources["Money"] = 0
UNITS = ["mL", "mL", "g", "$"]


# Support for 'print report' function to view available resources
def get_formatted_report(res):
    global UNITS
    i = -1
    for entry in resources:
        i += 1
        if UNITS[i] != "$":
            print(f"{entry}: {resources[entry]}{UNITS[i]}")
        else:
            print(f"{entry}: {UNITS[i]}{resources[entry]:.2f}")


# Check if viable order
def viable_order(order, available_resources):
    global MENU
    ordered_item = MENU[order]["ingredients"]

    i = -1
    for res in available_resources:
        i += 1
        if i < 3:
            try:
                amt_needed = ordered_item[res]
            except:
                amt_needed = 0
            
            if amt_needed > available_resources[res]:
                return False, res
    
    return True, res


# Collect change from customer
def collect_change():
    names = ["quarters", "dimes", "nickels", "pennies"]
    values = [0.25, 0.1, 0.05, 0.01]
    total_val = 0
    i = -1
    for coin in names:
        i += 1
        num_coins = int(input(f"How many {coin}?:  "))
        total_val += num_coins * values[i]
    return total_val

        
# Update resources after serving customer
def update_resources(item, res):
    global MENU
    ordered_item = MENU[item]["ingredients"]
    for cur_res in res:
        try:
            amt_needed = ordered_item[cur_res]
        except:
            amt_needed = 0
        
        if cur_res == "Money":
            amt_needed = MENU[item]["cost"] * -1
        res[cur_res] -= amt_needed

    return res
        

# TODO Prompt user - What would you like?
def coffee_runtime(menu, resources):
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
 # TODO Ability to turn off the coffee maching (off)   
    if user_prompt == "off":
        return
    elif user_prompt == "report":
        get_formatted_report(resources)
    else:
        [enough_resources, limiting_resource] = viable_order(user_prompt, resources)
        if enough_resources:
            print("Please insert coins")
            total_val = collect_change()
            if total_val > menu[user_prompt]["cost"]:
                change = total_val - menu[user_prompt]["cost"]
                print(f"Here is ${change:0.2f} in change")
                print(f"Here is your {user_prompt} ☕ enjoy!")
                resources = update_resources(user_prompt, resources)
            else:
                print(f"Sorry, that's not enough money. ${total_val:.2f} refunded")
        else:
            print(f"Sorry, there is not enough {limiting_resource}")
            
    # Continue running after each order/report request
    coffee_runtime(menu, resources)


coffee_runtime(MENU, resources)
