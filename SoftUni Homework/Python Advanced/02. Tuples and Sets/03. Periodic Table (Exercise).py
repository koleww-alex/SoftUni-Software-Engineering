N = int(input())
unique_elements = set()

for _ in range(N):
    compounds = input().split()
    for compound in compounds:
        unique_elements.add(compound)

for element in unique_elements:
    print(element)

# print('\n'.join(unique_elements))
