from collections import deque
elves = deque(map(int, input().split()))
materials = list(map(int, input().split()))
toys_made = 0
total_energy_used = 0
cnt = 0
while materials and elves:
    elf = elves.popleft()
    if elf < 5:
        continue
    cnt += 1
    material = materials.pop()
    if cnt % 3 == 0:
        if elf >= material * 2:
            if cnt % 5 == 0:
                total_energy_used += material * 2
                elf -= material * 2
                elves.append(elf)
            else:
                total_energy_used += material * 2
                elf -= material * 2
                elf += 1
                toys_made += 2
                elves.append(elf)
        else:
            materials.append(material)
            elf *= 2
            elves.append(elf)

    elif cnt % 5 == 0:
        if elf >= material:
            total_energy_used += material
            elf -= material
            elves.append(elf)
        else:
            materials.append(material)
            elf *= 2
            elves.append(elf)

    else:
        if elf >= material:
            toys_made += 1
            total_energy_used += material
            elf -= material
            elf += 1
            elves.append(elf)
        else:
            materials.append(material)
            elf *= 2
            elves.append(elf)


print(f'Toys: {toys_made}')
print(f'Energy: {total_energy_used}')
if elves:
    print(f'Elves left: {", ".join(str(x) for x in elves)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')
