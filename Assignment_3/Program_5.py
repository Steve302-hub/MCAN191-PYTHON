
"Count Consecutive Increase Blocks"

count = 1
no_block = 1
max_block_length = 1
block_length = 1

while count <= 8:
    num = int(input("Enter your no: "))
    if count == 1:
        value1 = num
    else:
        if num > value1:
            block_length += 1
            value1 = num
        else:
            no_block += 1
            if block_length > max_block_length:
                max_block_length = block_length
            block_length = 1
            value1 = num
    count += 1

print("No of increasing-blocks:", no_block)
print("Length of the longest block:", max_block_length)
