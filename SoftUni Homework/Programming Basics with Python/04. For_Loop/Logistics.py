number_cargo = int(input())
total_cargo_weight = 0
price_per_ton = 0
r1 = 0
r2 = 0
r3 = 0

for _ in range(1, number_cargo + 1):
    cargo_weight = int(input())
    total_cargo_weight += cargo_weight

    if cargo_weight <= 3:
        price_per_ton += 200 * cargo_weight
        r1 += cargo_weight
    elif 4 <= cargo_weight <= 11:
        price_per_ton += 175 * cargo_weight
        r2 += cargo_weight
    else:
        price_per_ton += 120 * cargo_weight
        r3 += cargo_weight

average_ton_price = price_per_ton / total_cargo_weight
p1 = (r1 / total_cargo_weight) * 100
p2 = (r2 / total_cargo_weight) * 100
p3 = (r3 / total_cargo_weight) * 100

print(f"{average_ton_price:.2f}")
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
