"""
"Digit-Extractor and Digit-Stats from Mixed String"

Problem: Given a string that may contain letters, digits, punctuation, spaces etc., extract all digit characters, treat them as numbers (single digits), then compute and output: (1) their sum, (2) their average (as float), (3) their maximum digit, (4) their minimum digit. If no digits — print an appropriate message.
"""

st = input("Enter a string: ")

num = []
flag = True

for ch in st:
    if chr(48) <= ch <= chr(57):
        num.append(int(ch))

if len(num) == 0:
    flag = False

if flag:
    add = 0

    for n in num:
        add += n

    avg = add // len(num)

    maxi = 0

    for n in num:
        if maxi < n:
            maxi = n

    mini = num[0]

    for i in range(1, len(num)):
        if mini > num[i]:
            mini = num[i]

    print("Sum:", add)
    print("Average:", avg)
    print("Maximum:", maxi)
    print("Minimum:", mini)
else:
    print("There's no numbers in string")
