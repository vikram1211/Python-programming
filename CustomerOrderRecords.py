#Adding a new customer.
#Adding a new order to an existing customer.
#Adding items to an existing order.
#Displaying the total cost for a given customer's orders.


def get_customer(customers):
    name=input('enter the customer name ')
    if name not in customers:
        customers[name]={}
    return name

def New_order(customers,name):
    order_id=input("enter the order number ")
    print(customers)
    if order_id in customers[name]:
        print('order number already exists')
        return
    customers[name][order_id]=Add_items()

def Add_items():
    items={}
    while True:
        name=input("enter the name of the item ")
        price=float(input("enter the price of the item "))
        items[name]=price
        a=input("provide yes if you want to add another item ")
        if a.lower() != 'yes':
            break
    return items

def display_orders(customers):
    for names,orders in customers.items():
        print(f"{names}:")
        for order_id,items in orders.items():
            print(f"order_{order_id}:")
            t=0
            for item, price in items.items():
                print(f"{item}:${price:.2f}")
            print(f"Total: ${sum(items.values()):.2f}")


def main():
    customers={}
    while True:
        name=get_customer(customers)
        New_order(customers,name)
        if input("Enter 'yes' to add orders for another customer, anything else to finish: ").lower() != 'yes':
            break
    display_orders(customers)

main()

