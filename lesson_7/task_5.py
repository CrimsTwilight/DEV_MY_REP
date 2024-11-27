"""
5. Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""


from functools import reduce
from operator import __add__


rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

print(reduce(__add__, list(map(lambda x: x["length"] * x["width"], rooms))))
