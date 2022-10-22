file_path = './sub_dir/text.txt'
try:
    with open(file_path, 'r') as file:
        print('File found')
except FileNotFoundError:
    print('File not found')
