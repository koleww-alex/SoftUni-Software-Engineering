from collections import defaultdict
characters = "".join(input().split(" "))
my_dict = defaultdict(int)

for ch in characters:
    my_dict[ch] += 1

print("\n".join(f"{key} -> {value}" for key, value in my_dict.items()))

# dictionary = {}
# for ch in characters:
#     if ch not in dictionary:
#         dictionary[ch] = 0
#     dictionary[ch] += 1
#
# print("\n".join(f"{key} -> {value}" for key, value in dictionary.items()))
