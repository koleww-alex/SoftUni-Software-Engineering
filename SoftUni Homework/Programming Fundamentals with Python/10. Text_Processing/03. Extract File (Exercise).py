file_location = input().split("\\")
name, extension = file_location[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
