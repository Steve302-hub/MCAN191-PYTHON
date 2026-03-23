
"Anagram-Group Detection"

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = []

for word in words:
    placed = False

    for group in groups:
        if sorted(word) == sorted(group[0]):
            group.append(word)
            placed = True
            
            break
    if not placed:
        groups.append([word])

print(groups)
