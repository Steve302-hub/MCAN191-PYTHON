
"Longest Increasing-Digit-Sum Substring (Contiguous)"



s = input("Enter a string: ")

new_s = ""
no_ls = []

for ch in s:
    if ch != " ":
        new_s += ch
    else:
        no_ls.append(new_s)
        new_s = ""

no_ls.append(new_s)

sum_ls = []

for i in range(len(no_ls)):
    dig_s = 0
    
    for ch in no_ls[i]:
        dig_s += int(ch)

    sum_ls.append(dig_s)

max_ln = 1
curr_ln = 1
end = 0

for i in range(1, len(sum_ls)):
    if sum_ls[i] > sum_ls[i - 1]:
        curr_ln += 1
    else:
        curr_ln = 1
    
    if max_ln < curr_ln:
        max_ln = curr_ln
        end = i

start = end - max_ln + 1

for i in range(start, end + 1):
    print(no_ls[i], end = " ")

print("\nLength:", max_ln)
