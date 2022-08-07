import re
text = input()
pattern = r"((www\.)([A-Za-z0-9]+\-?[A-Za-z0-9]+)+(\.[a-z]+)+)"
list_of_matches = []
while text:
    matches = re.findall(pattern, text)
    for match in matches:
        print(match[0])

    text = input()
