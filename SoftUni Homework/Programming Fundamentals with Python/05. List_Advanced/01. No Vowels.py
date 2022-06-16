string = input()

vowels = ["a", "o", "u", "e", "i"]

filtered_list = []

for element in range(len(string)):
    ch = string[element]
    if ch.lower() not in vowels:
        filtered_list.append(ch)

print("".join(filtered_list))

