command = input()
caesar_word = ""
for ch in command:
    new_ch = ord(ch) + 3
    caesar_word += chr(new_ch)

print(caesar_word)
