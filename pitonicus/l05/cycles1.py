# i = 0
# while i <= 10:
#     i = i + 1 
#     print(i)

# name = ""
# while name != "Рукижат":
#     name = input("Введите имя: ")
#     print("Вы не подходите")
# print("Все верно")

while True:
    # print("Вы все умрете")
    name = input("Введите имя: ")
    if name == "Рукижат":
        print("Все верно")
        break
    if name == "Саид":
        print("Вы не совсем подходите")
        continue
    print("Вы не подходите")