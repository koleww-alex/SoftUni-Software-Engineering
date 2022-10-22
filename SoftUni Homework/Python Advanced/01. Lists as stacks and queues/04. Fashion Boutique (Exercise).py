clothing = list(map(int, input().split()))
max_size_of_rack = int(input())
temporary_size = max_size_of_rack
racks_used = 1
while clothing:
    current_cloth = clothing.pop()

    if current_cloth > temporary_size:
        racks_used += 1
        temporary_size = max_size_of_rack
        temporary_size -= current_cloth

    elif current_cloth <= temporary_size:
        temporary_size -= current_cloth

print(racks_used)
