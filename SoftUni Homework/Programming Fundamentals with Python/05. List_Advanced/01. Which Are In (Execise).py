list_of_substrings = input().split(", ")
list_of_strings = input().split(", ")

filtered_strings = []

for first_word in list_of_substrings:
    for second_word in list_of_strings:
        if first_word in second_word:
            filtered_strings.append(first_word)
            break

print(filtered_strings)
