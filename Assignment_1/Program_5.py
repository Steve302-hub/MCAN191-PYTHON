num = int(input("Enter any 5 digit number: "))
s = 0
# 1st digit
d1 = num // 10000
num = num % 10000
d1 = (d1 + 1) % 10
s = s + d1 * 10000
# 2nd digit
d2 = num // 1000
num = num % 1000
d2 = (d2 + 1) % 10
s = s + d2 * 1000
# 3rd digit
d3 = num // 100
num = num % 100
d3 = (d3 + 1) % 10
s = s + d3 * 100
# 4th digit
d4 = num // 10
num = num % 10
d4 = (d4 + 1) % 10
s = s + d4 * 10
# 5th digit
d5 = num
d5 = (d5 + 1) % 10
s = s + d5 * 1
print(s)
