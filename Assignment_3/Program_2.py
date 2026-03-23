
"Print Multiples with Skip"

n = int(input("Enter a range: "))
k = int(input("Enter an integer: "))

numbers = ""
count = 0

for i in range(n):
    num = int(input("Enter a number: "))

    if num % k == 0:
        count += 1
        
        # Skip the first multiple
        if count > 1:
            numbers = numbers + str(num) + " "

print(numbers)
