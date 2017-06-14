name = input("Введите имя: ")

if (len(name) >= 30 or name == "Полиграф") and \
    not name == "30Букв30Букв30Букв30Букв30Букв30Букв30Букв30Букв30Букв30Букв":
    print("Кошмарное имя")
# elif len(name) > 10 and len(name) < 15:
elif  10 < len(name) < 15:
    print("Длинное имя")
else:
    print("Нормальное имя")
