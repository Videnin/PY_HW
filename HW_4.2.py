import random

# Генерация числа с длинной 3-10, диапазон 1-100
original_list = random.sample(range(1, 101), random.randint(3, 10))
print("Original list:", original_list)

# Создание нового списка
new_list = [original_list[0], original_list[2], original_list[-2]]
print("New list:", new_list)
