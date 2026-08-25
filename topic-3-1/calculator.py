# Set the price for each item
BURGER_PRICE = 12.00
CHIPS_PRICE = 2.00
SKITTLES_PRICE = 1.50
HERSHEYS_PRICE = 1.50

burgers = int(input("Amount of burgers purchased: "))
chips = int(input("Amount of chips purchased: "))
skittles = int(input("Amount of skittles purchased: "))
hersheys = int(input("Amount of hersheys purchased: "))

total_items = burgers + chips + skittles + hersheys
total_cost = (
    (burgers * BURGER_PRICE) + 
    (chips * CHIPS_PRICE) + 
    (skittles * SKITTLES_PRICE) + 
    (hersheys * HERSHEYS_PRICE)
)

# Print the results
print("Total items purchased:", total_items)
print(f"Total cost: ${total_cost:.2f}")



#