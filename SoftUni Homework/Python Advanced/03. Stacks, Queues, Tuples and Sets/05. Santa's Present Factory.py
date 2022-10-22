from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
toys_crafted = {}

while materials and magic:
    total_magic_level = materials[-1] * magic[0]

    if total_magic_level == 150:
        materials.pop()
        magic.popleft()
        if 'Doll' not in toys_crafted:
            toys_crafted['Doll'] = 0
        toys_crafted['Doll'] += 1

    elif total_magic_level == 250:
        materials.pop()
        magic.popleft()
        if 'Wooden train' not in toys_crafted:
            toys_crafted['Wooden train'] = 0
        toys_crafted['Wooden train'] += 1

    elif total_magic_level == 300:
        materials.pop()
        magic.popleft()
        if 'Teddy bear' not in toys_crafted:
            toys_crafted['Teddy bear'] = 0
        toys_crafted['Teddy bear'] += 1

    elif total_magic_level == 400:
        materials.pop()
        magic.popleft()
        if 'Bicycle' not in toys_crafted:
            toys_crafted['Bicycle'] = 0
        toys_crafted['Bicycle'] += 1

    else:
        flag = False

        if magic[0] == 0:
            flag = True
            magic.popleft()

        if materials[-1] == 0:
            flag = True
            materials.pop()

        if flag:
            continue

        if total_magic_level < 0:
            sum_value = materials.pop() + magic.popleft()
            materials.append(sum_value)

        elif total_magic_level > 0:
            magic.popleft()
            materials[-1] += 15

if 'Doll' in toys_crafted and 'Wooden train' in toys_crafted or 'Teddy bear' in toys_crafted and 'Bicycle' in toys_crafted:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    reversed_materials = []
    for _ in range(len(materials)):
        reversed_materials.append(materials.pop())

    print(f'Materials left: {", ".join(str(x) for x in reversed_materials)}')
if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')

for key, value in sorted(toys_crafted.items()):
    print(f'{key}: {value}')
