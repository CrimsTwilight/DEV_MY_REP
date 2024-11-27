"""
2. Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""


list_of_numbers = [-3, -2, -1, 0, 1, 2, 3]
print(list_of_numbers)
print(list(filter(lambda x: x > 0, list_of_numbers)))
