
"Sub-list Removal Variants"

length = int(input("Enter no of elements: "))

ls = []

for _ in range(length):
    ls.append(int(input("Enter element: ")))

unq_ls = []

for n in ls:
    if n not in unq_ls:
        unq_ls.append(n)

print("Given List:", unq_ls)

for i in range(len(unq_ls)):
    new_ls = []

    for j in range(len(unq_ls)):
        if i != j:
            new_ls.append(unq_ls[j])
    
    print(new_ls)
