N = int(input())
longest_intersection = []

for _ in range(N):
    first_range, second_range = input().split('-')
    first_range_start, first_range_end = first_range.split(',')
    second_range_start, second_range_end = second_range.split(',')
    first_set, second_set = set(), set()
    for i in range(int(first_range_start), int(first_range_end) + 1):
        first_set.add(i)

    for i in range(int(second_range_start), int(second_range_end) + 1):
        second_set.add(i)

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

str_numbers = [str(x) for x in longest_intersection]

print(f'Longest intersection is [{", ".join(str_numbers)}] with length {len(longest_intersection)}')
