def sum_even_indices(nums):
    if not nums:
        return 0

    even_sum = sum(nums[i] for i in range(0, len(nums), 2))

    result = even_sum * nums[-1]

    return result


array = [23, 79, 65, 132, 5]
result = sum_even_indices(array)
print("Result:", result)

