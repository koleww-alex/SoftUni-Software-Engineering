def fibonacci():
    nums = 0, 1

    while True:
        current_sum = sum(nums)
        second_number = nums[1]

        yield nums[0]
        nums = second_number, current_sum
