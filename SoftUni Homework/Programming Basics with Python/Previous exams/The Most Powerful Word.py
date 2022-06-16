from sys import maxsize
from math import floor

command = input()

list1 = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

max_number = -maxsize
word = ""

while command != "End of words":
    total_ascii_value = 0
    ch_cnt = 0
    ch = ""
    for ch in command:
        ascii_value = ord(ch)
        total_ascii_value += ascii_value
    if command[0] in list1:
        total_ascii_value *= len(command)
    if command[0] not in list1:
        total_ascii_value /= len(command)
        floor(total_ascii_value)
    if total_ascii_value > max_number:
        max_number = total_ascii_value
        word = command

    command = input()

print(f"The most powerful word is {word} - {max_number}")
