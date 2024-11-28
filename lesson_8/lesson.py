try:
    # print('1' + 1)
    # print(sum)
    print(1 / 0)
except NameError:
    print("sum не существует")
except ZeroDivisionError:
    print("Вы не можете разделить на 0")
except:
    print("Что-то пошло не так...")