import re
text = input()
threshold = 1
threshold_pattern = r'\d'
emoji_pattern = r'::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*'
matches = re.findall(threshold_pattern, text)
for number in matches:
    threshold *= int(number)

emojis = re.findall(emoji_pattern, text)
emojis_found = len(emojis)
cool_emojis = []

for emoji in emojis:
    emoji_points = 0
    for ch in emoji:
        if ch != ':' and ch != '*':
            emoji_points += ord(ch)
    if emoji_points >= threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
print(f'{emojis_found} emojis found in the text. The cool ones are:')
print('\n'.join(cool_emojis))
