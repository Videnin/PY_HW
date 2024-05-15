def move_zeros(nums):
    # указатели
    left = 0
    right = len(nums) - 1

    # Перемещаем (НЕ) нули
    while left < right:
        if nums[left] == 0:
            nums.pop(left)
            nums.append(0)
            right -= 1
        else:
            left += 1

    return nums


# TЕСТ
nums = [0, 1, 0, 3, 12, 0, 5, 0, 6]
result = move_zeros(nums)
print("Result:", result)
