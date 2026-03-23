
"Digit-Sum Recursion with Loop"

choice = True
total = 0

while choice == True:
    n = int(input("Enter a positive integer: "))

    if n <= 0:
        choice = False
    else:
        tmp = n
        add = 0
        count = 0
        flag = True

        # Loop until sum is a single digit
        while flag == True:
            add=0

            while tmp != 0:
                add = add + (tmp % 10)
                tmp = tmp // 10

            if add > 9:
                tmp = add
                count = count + 1
            else:
                flag = False

        print("Iterations:", count)
        print("Final digit:", add)

        total += 1

print("Total numbers processed:", total)
