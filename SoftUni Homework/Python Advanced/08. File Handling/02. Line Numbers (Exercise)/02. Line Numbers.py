from string import punctuation
text_path = './text.txt'
output_path = './output.txt'
with open(text_path, 'r') as file:
    text = file.readlines()

with open(output_path, 'a') as file:
    for i in range(len(text)):
        letters = 0
        marks = 0
        for ch in text[i]:
            if ch.isalpha():
                letters += 1
            elif ch in punctuation:
                marks += 1

        sentence = f'Line: {i + 1} {"".join(text[i]).strip()} ({letters})({marks})\n'
        file.write(sentence)
