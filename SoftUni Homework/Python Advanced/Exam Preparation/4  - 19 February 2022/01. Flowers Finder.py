from collections import deque

words = {"1": ['rose', 0], "2": ['tulip', 0], "3": ['lotus', 0], "4": ['daffodil', 0]}
output = {'1': 'rose', '2': 'tulip', '3': 'lotus', '4': 'daffodil'}
vowels = deque(input().split())
consonants = deque(input().split())
word_found = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        if vowel in words[word][0]:
            words[word][1] += 1
            words[word][0] = words[word][0].replace(vowel, '')

        if consonant in words[word][0]:
            words[word][1] += 1
            words[word][0] = words[word][0].replace(consonant, '')

        if words[word][0] == '':
            print(f'Word found: {output[word]}')
            word_found = True
            break
    if word_found:
        break

if not word_found:
    print('Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
