"""
"List-of-Lists Aggregation: Sales Data"

Problem: Suppose you receive daily sales data for several products over $n$ days. The data is represented as a list of lists: each inner list corresponds to a day and contains sales numbers (integers) for different products. For example:
    sales = [
        [5, 3, 0, 2], # day 1: product1 sold 5, product2 sold 3, product3 sold 0, product4 sold 2
        [7, 0, 2, 1], # day 2 ...
        [0, 1, 4, 0],
        ...
    ]
Write a program that:
    a. Computes total sales per product over all days.
    b. Identifies product(s) with maximum total sales and product(s) with minimum total sales.
    c. Prints a summary: for each product — total sales; then which product(s) sold the most in total, which the least.
Input: A list of lists of non-negative integers; you may also take number of days and number of products, or infer from data shape.
Output: Summary as described.
"""

days = int(input("Enter number of days: "))
products = int(input("Enter number of products: "))

sales = []

# Taking each product sales per day
for i in range(days):
    print(f"Day {i + 1}")
    day_sales = []
    
    for j in range(products):
        num = int(input(f"Enter product {j + 1} sale: "))
        day_sales.append(num)
    
    sales.append(day_sales)

print("Daily Sales Data:", sales)

total = []

# Total sales per product over all days
for i in range(products):
    sum = 0

    for j in range(days):
        sum += sales[j][i]

    total.append(sum)

for i in range(len(total)):
    print(f"Total sales of product {i + 1}: {total[i]}")

max_product = 0
min_product = 0

for i in range(len(total)):
    # Product with maximum sales
    if total[max_product] < total[i]:
        max_product = i
    
    # Product with minimum sales
    if total[min_product] > total[i]:
        min_product = i

print(f"Product {max_product + 1} has maximum sales")
print(f"Product {min_product + 1} has minimum sales")
