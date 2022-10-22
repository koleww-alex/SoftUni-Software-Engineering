list_of_nums = list(input().split('|'))
sub_lists = []

# split() -> splits the items by one or more white spaces !
for item in list_of_nums[::-1]:
    sub_lists.extend(item.split())

print(' '.join(sub_lists))
