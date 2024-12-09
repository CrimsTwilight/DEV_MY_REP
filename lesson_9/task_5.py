"""
5. В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""


with open(file='students.txt', encoding='UTF-8') as file:
    for line in file:
        name, surname, grade = line.split()

        if int(grade) < 3:
            print(f'{surname} {name} - {grade}')
