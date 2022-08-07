import re
text = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"
x = re.findall(pattern, text, re.IGNORECASE)
print(len(x))
