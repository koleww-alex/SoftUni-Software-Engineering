list_of_strings = input().split()
palindrome_word = input()

list_of_palindromes = []

for string in list_of_strings:
    if string == string[::-1]:
        list_of_palindromes.append(string)

print(list_of_palindromes)
palindrome_word_cnt = list_of_palindromes.count(palindrome_word)
print(f"Found palindrome {palindrome_word_cnt} times")
