def reversed_word(list_of_words: list):
    return "".join(f"{word} = {word[::-1]}" for word in list_of_words)


words = input().split()
while "end" not in words:
    print(reversed_word(words))
    words = input().split()


# words = input()
# while "end" not in words:
#     print(f"{words} = {words[::-1]}")
#     words = input()
#
