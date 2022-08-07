import re
text = input()
pattern = r"((?<=\s)[a-z0-9]+[\-\.\_\,]?[a-z0-9]+@[a-z]+[\-]?[a-z]+([\.][a-z]+)+)"
matches = re.findall(pattern, text)
print("\n".join(match[0] for match in matches))

# for match in matches:
#     # if match:
#     print(match[0])
