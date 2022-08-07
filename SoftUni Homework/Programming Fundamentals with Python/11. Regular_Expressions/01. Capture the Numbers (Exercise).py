import re
pattern = r"\d+"
command = input()
while command:
    match = re.findall(pattern, command)
    if match:
        print(" ".join(match), end=" ")

    command = input()

