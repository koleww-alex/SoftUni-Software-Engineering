file_path = 'sub_dir/numbers.txt'
result = 0
with open(file_path, 'r') as file:
    result += sum([int(x) for x in file])

print(result)
