"""
2. Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""


try:
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))
    operation = input("Выберите операцию (\"+\" / \"-\" / \"*\" / \"/\"): ").strip()

    if operation == '+':
        print(f"{number_1} + {number_2} = {number_1 + number_2}")
    elif operation == '-':
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
    elif operation == '*':
        print(f"{number_1} * {number_2} = {number_1 * number_2}")
    elif operation == '/':
        print(f"{number_1} / {number_2} = {number_1 / number_2: .3f}")
    else:
        print("Неправильная операция!")
except ValueError:
    print("Вы ввели не число, либо использовали неправильный разделитель!",
          "Для разделения дробных чисел пожалуйста используйте \".\"!", sep='\n')
except ZeroDivisionError:
    print("На ноль делить нельзя!")
