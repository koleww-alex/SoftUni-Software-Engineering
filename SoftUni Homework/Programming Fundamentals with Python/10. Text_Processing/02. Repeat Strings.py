def repeat(list_of_words: list):

    return "".join(word * len(word) for word in list_of_words)


words = input().split()
print(repeat(words))
