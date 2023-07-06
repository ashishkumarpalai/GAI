from tabulate import tabulate

snacks = {}
sales = {}

def display_snacks():
    if snacks:
        table = []
        for snack_id, snack_info in snacks.items():
            snack_name = snack_info['snack_name']
            price = snack_info['price']
            availability = snack_info['availability']
            quantity = snack_info['quantity']
            table.append([snack_id, snack_name, price, availability, quantity])
        print(tabulate(table, headers=["ID", "Snack Name", "Price", "Availability", "Quantity"], tablefmt="grid"))
    else:
        print("--------------------------------------")
        print("Snack inventory is empty.")
        print("--------------------------------------")

def add_snack():
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the snack available? (yes/no): ")
    quantity = int(input("Enter the quantity: "))

    snacks[snack_id] = {
        'snack_name': snack_name,
        'price': price,
        'availability': availability,
        'quantity': quantity
    }

    sales[snack_id] = 0
    print("--------------------------------------")
    print("Snack added to the inventory.")
    print("--------------------------------------")

def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")

    if snack_id in snacks:
        del snacks[snack_id]
        del sales[snack_id]
        print("--------------------------------------")
        print("Snack removed from the inventory.")
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print("Snack ID not found.")
        print("--------------------------------------")

def update_availability():
    snack_id = input("Enter the snack ID to update availability: ")

    if snack_id in snacks:
        availability = input("Is the snack available? (yes/no): ")
        snacks[snack_id]['availability'] = availability
        print("--------------------------------------")
        print("Availability updated.")
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print("Snack ID not found.")
        print("--------------------------------------")

def sell_snack():
    snack_id = input("Enter the snack ID to sell: ")

    if snack_id in snacks:
        if snacks[snack_id]['availability'] == 'yes':
            if snacks[snack_id]['quantity'] > 0:
                snacks[snack_id]['quantity'] -= 1
                sales[snack_id] += 1
                print("--------------------------------------")
                print("Snack sold.")
                print("--------------------------------------")
            else:
                print("--------------------------------------")
                print("Snack is out of stock.")
                print("--------------------------------------")
        else:
            print("--------------------------------------")
            print("Snack is not available for sale.")
            print("--------------------------------------")
    else:
        print("--------------------------------------")
        print("Snack ID not found.")
        print("--------------------------------------")

while True:
    print("Welcome to the Canteen System!")
    print("1. Display Snacks")
    print("2. Add Snack")
    print("3. Remove Snack")
    print("4. Update Snack Availability")
    print("5. Sell Snack")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_snacks()
    elif choice == '2':
        add_snack()
    elif choice == '3':
        remove_snack()
    elif choice == '4':
        update_availability()
    elif choice == '5':
        sell_snack()
    elif choice == '6':
        print("--------------------------------------")
        print("Thank you for using the Canteen System. Goodbye!")
        print("--------------------------------------")
        break
    else:
        print("--------------------------------------")
        print("Invalid choice. Please try again.")
        print("--------------------------------------")
