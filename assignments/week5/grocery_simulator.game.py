import time
inventory = []
items_info = [
    {"name": "Chicken", "calories": "165", "protein": "31 g", "price": "5$"},
    {"name": "Broccoli", "calories": "55", "protein": "3.7 g", "price": "2$"},
    {"name": "Almonds", "calories": "579", "protein": "21.2 g", "price": "2$"},
    {"name": "Salmon", "calories": "208", "protein": "20 g", "price": "7$"},
    {"name": "Eggs", "calories": "155", "protein": "13 g", "price": "1$"},
    {"name": "Quinoa", "calories": "120", "protein": "4.1 g", "price": "1$"},
    {"name": "Greek Yogurt", "calories": "59", "protein": "10 g", "price": "2$"},
    {"name": "Brown Rice", "calories": "123", "protein": "2.7 g", "price": "1$"},
    {"name": "Tofu", "calories": "76", "protein": "8 g", "price": "3$"},
    {"name": "Lentils", "calories": "116", "protein": "9 g", "price": "2$"},
    {"name": "Peanut Butter", "calories": "588", "protein": "25 g", "price": "4$"},
]

item_name = ["Chicken","Broccoli","Almonds","Salmon","Eggs","Quinoa","Greek Yogurt","Brown Rice","Tofu","Lentils","Peanut Butter"]



 # length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5



# --- Functions ---

def show_inventory():
    print(inventory)
    pass

def show_room_items():
    print(item_name)
    pass

def pick_up():

    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Sorry, you don't have enough space")
        return
    item_pup= str(input("what item would you like to pick up?"))
    if item_pup in item_name:
        inventory.append(item_pup)
        print("You picked up " + item_pup)

    else:
        print("item not found in the room")
    pass



def drop():
    drop_item= str(input("what item would you like to drop?"))
    if drop_item in inventory:
        inventory.remove(drop_item)
        print("You dropped " + drop_item)

    else:
        print("item not found in your shopping cart")
    pass

def use():
    use_item= str(input("what item would you like to use?"))
    if use_item in inventory:
        print("Mhhhhhh",use_item,"tastes wonderful!")
        inventory.remove(use_item)
        time.sleep(1)
        print("deeeelicious")

    else:
        print("item not found in your shopping cart")

    pass

def examine():
    while len(inventory) >= 1:
        examine_item= str(input("What item would you like to examine?"))

        if examine_item not in inventory:
            print("Your item of choice is not in your inventory")
            break


        if examine_item == "Chicken":
            print (items_info[0])
            break

        elif examine_item == "Broccoli":
            print (items_info[1])
            break

        elif examine_item == "Almonds":
            print (items_info[2])
            break

        elif examine_item == "Salmon":
            print (items_info[3])
            break

        elif examine_item == "Eggs":
            print (items_info[4])
            break

        elif examine_item == "Quinoa":
            print (items_info[5])
            break

        elif examine_item == "Greek Yogurt":
            print (items_info[6])
            break

        elif examine_item == "Brown Rice":
            print (items_info[7])
            break

        elif examine_item == "Tofu":
            print (items_info[8])
            break

        elif examine_item == "Lentils":
            print (items_info[9])
            break

        elif examine_item == "Peanut Butter":
            print (items_info[10])
            break

        else:
            print("item not found")
    else:
        print("no item in your inventory")


    # you can only examine an item if it's in your inventory
    pass

def checkout():
    total = 0
    print("Checkout Summary:")
    for item in inventory:
        for info in items_info:
            if info["name"].lower() == item.lower():
                price_str = info["price"].replace("$", "")
                price = int(price_str)
                total += price
                print(f"- {info['name']}: {info['price']}")
                break
    print(f"\nTotal: {total}$")
    print("Thanks for shopping with us!\n")


# --- Game Loop ---

def game_loop():
    print("Welcome to the Grocery Store Game!, add different Products to your shopping cart and see the details")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: shopping cart, look, pickup [item], drop [item], use [item], examine [item], quit, checkout")
        elif command == "shopping cart":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command == "pickup":
            pick_up()
        elif command == "drop":
            drop()
        elif command =="use":
            use()
        elif command == "examine":
            examine()
        elif command == "checkout":
            checkout()
            break
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()