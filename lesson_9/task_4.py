"""
4. Напишите программу, которая получает на вход строку
с названием текстового файла и выводит на экран
содержимое этого файла, заменяя все запрещённые слова
звездочками. Запрещённые слова, разделённые символом
пробела, должны храниться в файле stop_words.txt.
Программа должна находить
запрещённые слова в любом месте файла, даже в середине
другого слова. Замена независима от регистра: если в списке
запрещённых есть слово exam, то замениться должны exam,
eXam, EXAm и другие вариации.
Пример: в stop_words.txt записаны слова: hello email
python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python
IS the programming language of thE future. My EMAIL is…
PYTHON as AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming
language of *** future. My ***** **... ****** ** awesome!!!!
"""
import re


input_file = input("Введите название файла для цензуры: ")
stop_words_file = 'stop_words.txt'

try:
    with open(file=stop_words_file, encoding='UTF-8') as file:
        stop_words = file.read().split()

    stop_words_pattern = "|".join(re.escape(word) for word in stop_words)
    regex_pattern = re.compile(stop_words_pattern, re.IGNORECASE)

    with open(file=input_file, encoding='UTF-8') as file:
        text_content = file.read()

    censored_text = regex_pattern.sub(lambda match: '*' * len(match.group()), text_content)
    print(censored_text)
except FileNotFoundError:
    print(f"Файл {input_file} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
