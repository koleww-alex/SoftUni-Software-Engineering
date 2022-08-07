elements = input().split(", ")
dictionary = {elements[i]: ord(elements[i]) for i in range(len(elements))}
print(dictionary)
