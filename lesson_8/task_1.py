"""
1. Реализовать программу для подсчёта индекса массы тела человека.
Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от попадания
в тот или иной диапазон. Использовать обработку исключений.
"""


try:
    height = float(input("Введите рост(м.): "))
    weight = float(input("Введите вес(кг.): "))
    result = weight / height ** 2

    if result < 16:
        print(f"Ваш ИМТ: {result:.1f} - значительный дефицит массы тела.")
    elif result < 18.5:
        print(f"Ваш ИМТ: {result:.1f} - дефицит массы тела.")
    elif result < 25:
        print(f"Ваш ИМТ: {result:.1f} - норма.")
    elif result < 30:
        print(f"Ваш ИМТ: {result:.1f} - лишний вес.")
    elif result < 35:
        print(f"Ваш ИМТ: {result:.1f} - ожирение первой степени.")
    elif result < 40:
        print(f"Ваш ИМТ: {result:.1f} - ожирение второй степени.")
    else:
        print(f"Ваш ИМТ: {result:.1f} - ожирение третьей степени.")
except ValueError:
    print("Вы ввели не число, либо использовали неправильный разделитель!",
          "Для разделения дробных чисел пожалуйста используйте \".\"!", sep='\n')
except ZeroDivisionError:
    print("На ноль делить нельзя!")
