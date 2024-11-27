"""
3. Дан список строк. С помощью filter() получить список тех
строк из исходного списка, которые являются палиндромами
(читаются в обе стороны одинаково, например, ’abcсba’)
"""


list_of_strings = ['abc', 'cba', 'abccba']
print(list_of_strings)
print(list(filter(lambda x: x == x[::-1], list_of_strings)))
