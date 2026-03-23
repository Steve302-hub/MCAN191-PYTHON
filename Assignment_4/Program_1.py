
"Interleaved Merge with Reversed Half"



s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")

new_s = ""

i = 0
j = -1

if len(s1) >= len(s2):
    for _ in range(len(s2)):
        new_s += s1[i]
        new_s += s2[j]

        i += 1
        j -= 1

    for _ in range(i, len(s1)):
        new_s += s1[i]

        i += 1
    
    print(new_s)
else:
    for _ in range(len(s1)):
        new_s += s1[i]
        new_s += s2[j]

        i += 1
        j -= 1

    for _ in range(len(s2) + j, -1, -1):
        new_s += s2[j]

        j -= 1

    print(new_s)
