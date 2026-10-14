orders = ["LAT003", "AME002", "LAT001", "CAP005"]
drinks_sold = 0
revenue = 0
order_count = 0

largest_order = 0
latte_orders = 0
found_cappuccino = False



for c in range(0, len(orders), 1):
    drink = orders[c][0:3]
    quantity = int(orders[c][3:6])
    drinks_sold = drinks_sold + quantity
    order_count = order_count + 1

    if quantity > largest_order:
        largest_order = quantity

    if drink == "LAT":
        revenue = revenue + quantity * 5
        latte_orders = latte_orders + 1
    elif drink == "AME":
        revenue = revenue + quantity * 4
    elif drink == "CAP":
        revenue = revenue + quantity * 6
        found_cappuccino = True

print("Drinks sold:", drinks_sold)
print("Revenue:", revenue)
print("Orders processed:", order_count)

print("Largest order:", largest_order)
print("Latte orders:", latte_orders)
if found_cappuccino:
    print("Cappuccino order found")
else:
    print("No cappuccino order found")
if revenue >= 40:
    print("Sales goal reached")
else:
    print("Sales goal not reached")



# I used string slicing to extract the drink type and quantity.
# The for loop processes each order and updates the totals.
# Adding a new drink type lets the program calculate more orders
# I can test the program by changing an order quantity and checking the total or what the ouoput ends up being.

#advanced:
# Changed CAP004 to CAP005 increased drinks sold from 10 to 11
#  revenue from $52 to $58.
# Improvement: In the future I could add more drink types and their prices to make it more advanced and have more variety.



