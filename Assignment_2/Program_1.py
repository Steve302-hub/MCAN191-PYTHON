"""
If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred.
"""

cost_price = float(input("Enter cost price: "))
sell_price = float(input("Enter sell price: "))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print("Total profit is", profit)
elif sell_price < cost_price:
    loss = cost_price - sell_price
    print("Total loss is", loss)
else:
    print("No profit, no loss")
