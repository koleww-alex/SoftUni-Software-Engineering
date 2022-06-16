expected_sum = int(input())
products = input()
products_sum = 0
cash_transactions = 0
credit_card_transactions = 0
day_cnt = 0
sum_reached = False
successful_transactions_cnt_cc = 0
successful_transactions_cnt_cs = 0

while products != "End":
    products = int(products)
    day_cnt += 1

    if day_cnt % 2 == 0:
        if products > 100:
            successful_transactions_cnt_cc += 1
            credit_card_transactions += products
            products_sum += products
            print("Product sold!")

        elif products < 10:
            print("Error in transaction!")

        else:
            successful_transactions_cnt_cc += 1
            credit_card_transactions += products
            products_sum += products
            print("Product sold!")

    else:
        if products > 100:
            print("Error in transaction!")

        elif products < 10:
            successful_transactions_cnt_cs += 1
            cash_transactions += products
            products_sum += products
            print("Product sold!")

        else:
            successful_transactions_cnt_cs += 1
            cash_transactions += products
            products_sum += products
            print("Product sold!")

    if products_sum >= expected_sum:
        sum_reached = True
        break

    products = input()

if sum_reached:
    average_cs = cash_transactions / successful_transactions_cnt_cs
    average_cc = credit_card_transactions / successful_transactions_cnt_cc
    print(f"Average CS: {average_cs:.2f}\n"
          f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
