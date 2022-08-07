import re

text = input()
pattern = r"\+359 [2] [0-9]{3} [0-9]{4}|\+359-[2]-[0-9]{3}-[0-9]{4}\b"
x = re.findall(pattern, text)
print(", ".join(x))
