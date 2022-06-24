secret_message = input().split()
deciphered_word = []
for element in secret_message:
    number = ""
    for ch in element:
        if ch.isdigit():
            number += ch
        else:
            break
    first_letter = chr(int(number))
    element = element.replace(number, "")

    if len(element) >= 2:
        final_message = first_letter + element[-1] + element[1:-1] + element[0]
    else:
        final_message = first_letter + element

    deciphered_word.append(final_message)

print(" ".join(deciphered_word))

