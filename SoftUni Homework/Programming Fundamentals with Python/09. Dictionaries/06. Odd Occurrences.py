from collections import defaultdict

# items = input().split()
# case_insensitive_items = {}
#
# for item in items:
#     lower_item = item.lower()
#
#     if lower_item not in case_insensitive_items:
#         case_insensitive_items[lower_item] = 0
#     case_insensitive_items[lower_item] += 1
#
# for key, value in case_insensitive_items.items():
#     if value % 2 != 0:
#         print(key, end=" ")

items = input().split()
dictionary = defaultdict(int)

for item in items:
    dictionary[item.lower()] += 1

print(" ".join([key for key, value in dictionary.items() if value % 2 != 0]))
