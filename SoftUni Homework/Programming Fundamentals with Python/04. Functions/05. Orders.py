product = input()
quantity = int(input())


def pricer(type_of_product, number):
    price = 0
    if type_of_product == "coffee":
        price = number * 1.50
    elif type_of_product == "coke":
        price = number * 1.40
    elif type_of_product == "water":
        price = number * 1.00
    elif type_of_product == "snacks":
        price = number * 2.00

    return price


print(f"{pricer(product, quantity):.2f}")
