"""
1. Работа с модулем os.
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
● Вывести имя вашей ОС
● Вывести путь до папки, в которой вы находитесь
● Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений
● После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт»
● Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt»
● Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.
"""
import os
from pathlib import Path


path = os.getcwd()
stats = {}

print(f"Имя ОС: {os.name}")
print(f"Путь до текущей папки: '{path}'")

for file in os.listdir(path):
    if os.path.isfile(file):
        extension = str(Path(file).suffix)[1:]
        if extension != "py":
            if not os.path.exists(extension):
                os.mkdir(extension)

            new_file = "some_" + file
            os.rename(file, new_file)
            os.replace(new_file, os.path.join(extension, new_file))
            print(f"Файл {file} был переименован в {new_file}")

            stats[extension] = {"count": 0, "size": 0}
            file_size = os.path.getsize(os.path.join(extension, new_file))
            stats[extension]["count"] += 1
            stats[extension]["size"] += file_size

for extension, data in stats.items():
    size_gb = data["size"] / (1024 ** 3)
    print(f"В папку с {extension} - файлами перемещено {data['count']} файлов, "
          f"их суммарный размер - {size_gb:.1f} ГБ")
