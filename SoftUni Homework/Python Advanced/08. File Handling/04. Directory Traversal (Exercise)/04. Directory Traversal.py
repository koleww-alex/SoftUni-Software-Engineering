from os import listdir, path


def extract_extensions(first_subdir=False):
    for file_name in listdir(directory):
        file = path.join(directory, file_name)

        if path.isfile(file):
            current_extension = file_name.split('.')[-1]

            if current_extension not in founded_extensions:
                founded_extensions[current_extension] = []
            founded_extensions[current_extension].append(file_name)

        elif path.isdir(file) and not first_subdir:
            extract_extensions(True)


directory = input()
founded_extensions = {}
result_dict = {}

extract_extensions()

sorted_extensions = sorted(founded_extensions.items(), key=lambda x: x[0])

for extension, files in sorted_extensions:
    result_dict[f'.{extension}'] = []

    for file in sorted(files):
        result_dict[f'.{extension}'].append(f'- - - {file}\n')

folder_name = 'result_folder.txt'
with open(folder_name, 'w') as file:
    for key, val in result_dict.items():
        file.write(key + '\n' + "".join(val))
