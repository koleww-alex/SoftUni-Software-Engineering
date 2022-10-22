cycles = list(map(int, input().split(', ')))
index = int(input())
searched_cycle = cycles[index]
total_cycles = 0
nums_before_our = 0

for i in range(index):
    if cycles[i] == cycles[index]:
        nums_before_our += 1

for _ in range(len(cycles)):
    min_cycle = min(cycles)
    if searched_cycle > min_cycle:
        total_cycles += min_cycle
        cycles.remove(min_cycle)

    elif searched_cycle == min_cycle:
        for _ in range(nums_before_our + 1):
            cycles.remove(min_cycle)
            total_cycles += min_cycle
        break
print(total_cycles)
