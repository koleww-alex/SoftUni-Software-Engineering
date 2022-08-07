from collections import defaultdict
number_of_synonyms = int(input())
synonyms = defaultdict(list)

for _ in range(number_of_synonyms):
    key, value = input(), input()
    synonyms[key].append(value)

print("\n".join(f"{key} - {', '.join(value)}" for key, value in synonyms.items()))
