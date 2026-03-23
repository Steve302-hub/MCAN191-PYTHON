"""
"Sliding Window Average & Variance Tracker"

Problem: Given a long list of numbers (floats or ints) representing, say, daily measurements (temperature, sales, or sensor readings), implement a "sliding window" algorithm: for a window size k, compute for each window position the average and variance (or standard deviation) of the numbers in that window. Output a list of tuples (average, variance) for all valid windows.
Input: A list of numbers (length >= k), integer window size k.
Output: A list of tuples: (avg, variance) for each position from start to len(list) - k + 1.
"""

length = int(input("Enter length of the list: "))
k = int(input("Enter the window size: "))

ls = []

for i in range(length):
    num = int(input(f"Enter element of A: "))
    ls.append(num)

result = []

for i in range(length - k + 1):
    window = ls[i : i + k]

    avg = sum(window) / k

    var_sum = 0
    
    for x in window:
        var_sum += (x - avg) ** 2

    var = var_sum / k

    result.append((avg , var))

print(result)
