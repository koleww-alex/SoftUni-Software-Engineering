input_path = 'input.txt'
symbols = ["-", ",", ".", "!", "?"]
cnt = 0
with open(input_path, 'r') as file:
    text = file.readlines()

for i in range(0, len(text), 2):
    for symbol in symbols:
        text[i] = text[i].replace(symbol, '@')
    print(*text[i].split()[::-1])
