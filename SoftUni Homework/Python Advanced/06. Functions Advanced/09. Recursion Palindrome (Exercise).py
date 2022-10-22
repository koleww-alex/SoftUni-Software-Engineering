def palindrome(word: str, index: int):
    if index == len(word) // 2:
        return f'{word} is a palindrome'

    elif word[index] != word[-1 - index]:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)
