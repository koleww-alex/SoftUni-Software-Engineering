from math import floor
biscuits_per_day_per_worker = int(input())
number_of_workers = int(input())
total_biscuits_enemy = int(input())

total_biscuits = 0

for day in range(1, 30 + 1):
    if day % 3 == 0:
        total_biscuits += floor((number_of_workers * biscuits_per_day_per_worker) * 0.75)
    else:
        total_biscuits += floor(number_of_workers * biscuits_per_day_per_worker)

print(f"You have produced {total_biscuits} biscuits for the past month.")

diff = abs(total_biscuits - total_biscuits_enemy)
percent_diff_more = (diff / total_biscuits_enemy) * 100

if total_biscuits > total_biscuits_enemy:
    print(f"You produce {percent_diff_more:.2f} percent more biscuits.")
else:
    print(f"You produce {percent_diff_more:.2f} percent less biscuits.")
