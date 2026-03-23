
"Balanced-String Test (All chars present)"



a = input("Enter 1st string: ")
b = input("Enter 2nd string: ")

num = []
flag = True

for c in a:
    if c not in b:
        flag = False
        num.append(c)

print(flag)
print(num)
