import re
pattern = r'[a-zA-z\']+'
words_dict = {}
words_path = 'words.txt'
with open(words_path, 'r') as file:
    words = file.read().split()

for word in words:
    words_dict[word.lower()] = 0

input_path = 'input.txt'
with open(input_path, 'r') as file:
    text = re.findall(pattern, file.read().lower())

for word in text:
    if word in words_dict:
        words_dict[word] += 1

output_path = 'output.txt'

with open(output_path, 'w') as file:
    for key, val in sorted(words_dict.items(), key=lambda x: -x[1]):
        file.write(f'{key} - {val}\n')
