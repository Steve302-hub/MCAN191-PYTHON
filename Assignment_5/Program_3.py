"""
"Rotate & Shift-Merge Lists"

Problem: Given two lists of equal length, A and B, write a program that "rotates" list A by some number of positions k (right-rotation), then merges with B by adding corresponding elements, and finally returns the resulting list. For example:
    A = [1, 2, 3, 4, 5]
    B = [10, 20, 30, 40, 50]
    k = 2 # rotate A right by 2 => [4, 5, 1, 2, 3]
    result = [4 + 10, 5 + 20, 1 + 30, 2 + 40, 3 + 50] = [14, 25, 31, 42, 53]
Input: Two lists of equal length (integers), and integer k >= 0.
Output: A new list of sums after rotation and merging.
"""

length = int(input("Enter length of list A and B: "))

A = []
B = []

print("List A")
for i in range(length):
    num = int(input(f"Enter element of A: "))
    A.append(num)

print("List B")
for i in range(length):
    num = int(input(f"Enter element of B: "))
    B.append(num)

k = int(input("Enter no of positions to rotate: "))

result = []

A = A[k + 1 : ] + A[: k + 1]
print("Rotated list A:", A)

sum = 0

for i in range(length):
    sum = A[i] + B[i]

    result.append(sum)

print(result)
