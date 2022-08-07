import re
text = input()
pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b"
x = re.findall(pattern, text)
print("\n".join(f"Day: {element[0]}, Month: {element[2]}, Year: {element[3]}" for element in x))
