import datetime
inventory = []

def get_date():
    dt_now = datetime.datetime.now().strftime('%Y-%m-%d')
    return dt_now

def add_item():
    name = input('Enter item name: ')
    quantity =input('Enter item quantity: ')
    price = input('Enter item price: ')
    updated_date = get_date()
    item = {'name':name, 'quantity': quantity, 'price': price, 'updated_at': updated_date }
    inventory.append(item)
    print('Item added correctly')

def update_item():
    name = input('Enter item name to update: ')
    for item in inventory:
        if item['name'] == name:
            quantity = int(input('Entern quantity: '))
            price = float(input('Entern price: '))
            item['quantity'] = quantity
            item['price'] = price
            updated_date = get_date()
            item['updated_at'] = updated_date
            print('Item updated')
            return
    print('Item not found.')

def search_item():
    option = int(input('Search by: \n1. Name\n2. Quantity\n3. Price\n0. Other...'))
    if option == 1:
        name = input('Name to search: ')
        filtered_items = list(filter(lambda item: name.lower() in item['name'].lower(), inventory))
    elif option == 2:
        quantity = input('Quantity to search: ')
        filtered_items = list(filter(lambda item: quantity in str(item['quantity']), inventory))
    elif option == 3:
        price = input('Price to search: ')
        filtered_items = list(filter(lambda item: price in str(item['price']), inventory))
    else:
        print('Invalid option')
        return
    
    if len(filtered_items) >0:
        print('Search results: \n', filtered_items)

def sort_item():
    
    option = int(input('Sort by: \n1.Name\n2. Quantity\n3. Price\n0. Other...'))
    if option == 1:
        sorted_items = sorted(inventory, key=lambda item: item['name'])
    elif option == 2:
        sorted_items = sorted(inventory, key=lambda item: int(item['quantity']))
    elif option == 3:
        sorted_items = sorted(inventory, key=lambda item: float(item['price']))
    else:
        print('Invalid option')
        return
    print(f'Sorted items: \n {sorted_items}')

def show_inventory():
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print(' Welcome to our inventory')
    print('Name, Quantity,  Price,  Updated at' )
    for item in inventory:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'{item["name"]}, {item["quantity"]}, {item["price"]}, {item["updated_at"]}')
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')

def delete_item():
    removed = False
    option = input('Type the name of the item to delete:')
    for item in inventory:
        if item['name'] == option:
            inventory.remove(item)
            print(f'{option} was correctly deleted')
            removed = True
    if removed is False:
        print('Sorry, we could not find that item')
    
def get_total_value():
    total= 0
    for item in inventory:
        single_total = float(item['price'])* int(item['quantity'])
        total +=single_total
    print('----------------------')
    print('TOTAL: ', total)
    print('----------------------')

def menu():
    while True:
        print('\n --Inventory Management System ----')
        print('0. Exit')
        print('1. Add')
        print('2. Update ')
        print('3. Search ')
        print('4. Sort ')
        print('5. Show Inventory')
        print('6. Delete item')
        print('7. Get total value')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            add_item()
        elif choice == 2:
            update_item()
        elif choice == 3:
            search_item()
        elif choice == 4:
            sort_item()
        elif choice ==5:
            show_inventory()
        elif choice ==6:
            delete_item()
        elif choice ==7:
            get_total_value()
        elif choice == 0:
            print('Exiting...')
            break
        else:
            print('Please choose a valid option..')
            break

menu()