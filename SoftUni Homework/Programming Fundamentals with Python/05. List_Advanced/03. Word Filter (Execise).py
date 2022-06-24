list_of_stings = input().split()

filtered_strings = [string for string in list_of_stings if len(string) % 2 == 0]

print("\n".join(filtered_strings))

