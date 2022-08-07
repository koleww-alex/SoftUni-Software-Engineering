def filter_text(list_of_words: list, filtered_text: str):
    for word in list_of_words:
        filtered_text = filtered_text.replace(word, len(word) * "*")
    return filtered_text


banned_words = input().split(", ")
text = input()
print(filter_text(banned_words, text))
