
"Sum of All even and odd numbers"
n = int(input("Enter a number: "))

i = 1
sum_of_evens = 0
sum_of_odds = 0

while i <= n:
    if i % 2 == 0:
        sum_of_evens += i
    else:
        sum_of_odds += i
    i += 1

print("Sum of all even numbers:", sum_of_evens)
print("Sum of all odd numbers:", sum_of_odds)
