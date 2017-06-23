# while True:
#     try:
#         number = int(input("введите делитель: "))
#         print(7 / number)
#         break
#     except ValueError:
#         print("Введи число!!!") 
#     except ZeroDivisionError:
#         print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ, ДУБИНА")

# raise ZeroDivisionError

class ChakarError(Exception):
    pass

while True:
    try:
        name = input("Введите имя: ")
        if name.lower() == "чакар":
            raise ChakarError
        print(name, "молодец")
    except ChakarError: 
        print("фатальная ошибка нельзя в водить это слово")
        break
