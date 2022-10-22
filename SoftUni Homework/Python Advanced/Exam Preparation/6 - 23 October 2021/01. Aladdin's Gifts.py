from collections import deque
materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))
items = {
    'Gemstone': [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499],
}

crafted_items = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}
wedding_check = []
presents_made = False

while materials and magic:
    successful_craft = False
    material = materials[-1]
    magic_val = magic[0]
    current_sum = material + magic_val

    for item in items:
        if items[item][0] <= current_sum <= items[item][1]:
            materials.pop(), magic.popleft()
            crafted_items[item] += 1
            successful_craft = True
            break
    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = material * 2 + magic_val * 3
        else:
            current_sum = material * 2 + magic_val * 2

    elif current_sum > 499:
        current_sum /= 2

    if not successful_craft:
        for item in items:
            if items[item][0] <= current_sum <= items[item][1]:
                materials.pop(), magic.popleft()
                crafted_items[item] += 1
                break
        else:
            materials.pop(), magic.popleft()


for item, val in crafted_items.items():
    wedding_check.append(item), wedding_check.append(val)

for i in range(0, len(wedding_check), 4):
    if wedding_check[i + 1] and wedding_check[i + 3]:
        presents_made = True
        break

if presents_made:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')

for item in sorted(crafted_items):
    if crafted_items[item]:
        print(f'{item}: {crafted_items[item]}')
