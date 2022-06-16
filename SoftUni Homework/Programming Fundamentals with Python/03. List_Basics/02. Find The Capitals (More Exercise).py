text = input()
list1 = []

for i, ch in enumerate(text):
    if ch == ch.upper():
        list1.append(i)

print(list1)
