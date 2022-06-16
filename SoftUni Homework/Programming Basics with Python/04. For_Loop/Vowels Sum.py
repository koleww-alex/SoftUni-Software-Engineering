word = input()

total = 0

for num in word:
    if num == "a":
        total += 1
    if num == "e":
        total += 2
    if num == "i":
        total += 3
    if num == "o":
        total += 4
    if num == "u":
        total += 5
print(total)

