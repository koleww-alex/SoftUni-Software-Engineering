def positive_vs_negative(numbers: list):
    numbers = [int(x) for x in numbers]
    result_positive, result_negative = 0, 0
    for num in numbers:
        if num < 0:
            result_negative += num
        else:
            result_positive += num

    return result_positive, result_negative


positive_sum, negative_sum = positive_vs_negative(input().split())

print(negative_sum)
print(positive_sum)
if positive_sum > abs(negative_sum):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')

