string = input()
my_dict = {}
for ch in string:
    if ch not in my_dict:
        my_dict[ch] = string.count(ch)

for key, value in sorted(my_dict.items()):
    print(f'{key}: {value} time/s')
