
"Alternating Sequence Filter"

i = 1
flag = True

accepted_numbers = ""

while i <= 10:
    n = int(input("Enter a number: "))
    
    if n % 2 == 0:
        # Even numbers
        if flag == True:
            accepted_numbers = accepted_numbers + str(n) + " "
            flag = False
    else:
        # Odd numbers
        if flag == False:
            accepted_numbers = accepted_numbers + str(n) + " "
            flag = True
    
    i += 1

print(accepted_numbers)
