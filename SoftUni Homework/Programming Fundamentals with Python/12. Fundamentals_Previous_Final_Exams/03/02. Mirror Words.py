import re
pattern = r"(\#[A-Za-z]{3,}\#){2}|(\@[A-Za-z]{3,}\@){2}"
text = input()
list_of_pairs = []
valid_matches = 0
matches = re.finditer(pattern, text)
for match in matches:
    valid_matches += 1
    pair = match.group()
    pair = pair.replace("#", "")
    pair = pair.replace("@", "")
    first_word = pair[:len(pair) // 2]
    second_word = pair[len(pair) // 2:]
    if first_word[::-1] == second_word:
        list_of_pairs.append(first_word)
        list_of_pairs.append(second_word)

if valid_matches > 0:
    print(f"{valid_matches} word pairs found!")
    if len(list_of_pairs) > 0:
        print("The mirror words are:")
        print(", ".join(f"{list_of_pairs[i]} <=> {list_of_pairs[i + 1]}" for i in range(0, len(list_of_pairs), 2)))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
