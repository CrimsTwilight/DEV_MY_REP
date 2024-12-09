"""
3. Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""
import re
from collections import Counter


def find_most_frequently_word_in_file(text):
    counter = Counter(text)
    most_frequently_word, count = counter.most_common(1)[0]
    return most_frequently_word, count


input_file = 'example_for_task_3.txt'
output_file = 'most_frequently_word.txt'

try:
    with open(file=input_file, encoding="UTF-8") as infile, \
            open(file=output_file, mode='w', encoding="UTF-8") as outfile:
        for lines in infile:
            line = re.findall(r'\b\w+\b', lines.lower())
            if line:
                most_frequently_word, count = find_most_frequently_word_in_file(line)
                if count > 1:
                    outfile.write(f'Слово "{most_frequently_word}" встречается в строке {count} раз.\n')
                else:
                    outfile.write("Все слова в строке уникальны.\n")
            else:
                outfile.write("Пустая строка.\n")
except FileNotFoundError:
    print(f'Файл "{input_file}" не найден.')
except Exception as e:
    print(f"Произошла ошибка: {e}")
