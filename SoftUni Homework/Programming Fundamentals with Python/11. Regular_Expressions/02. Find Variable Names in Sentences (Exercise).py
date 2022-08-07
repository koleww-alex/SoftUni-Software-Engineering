import re
pattern = r"\b_([A-Za-z0-9]+)\b"
text = input()
x = re.findall(pattern, text)
print(",".join(x))
