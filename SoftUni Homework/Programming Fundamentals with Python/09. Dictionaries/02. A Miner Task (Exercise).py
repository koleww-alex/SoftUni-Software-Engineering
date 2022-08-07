list_of_countries = input().split(", ")
list_of_capitals = input().split(", ")
my_dictionary = {list_of_countries[i]: list_of_capitals[i] for i in range(0, len(list_of_capitals))}

for key, value in my_dictionary.items():
    print(f"{key} -> {value}")
