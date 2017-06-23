# while True:
#     try:
#         number = int(input("Введите число: "))
#         print(" 7 /",number,"=", 7 / number)
#         break
#     except ValueError:
#         print("Ты тупой, введи число!")
#     except ZeroDivisionError:
#         print("Твой интеллект тоже равен 0. На ноль не делится!!!")

# print("Привет")
# raise ZeroDivisionError

class SaaduError(Exception):
    pass

try:
    name = input("Введите имя: ")
    if name == "Сааду":
        raise SaaduError
    print("Ну ок")
except SaaduError:
    print("ФАТАЛЬНАЯ ОШИБКА. ВЫ ВВЕЛИ СААДУ")

