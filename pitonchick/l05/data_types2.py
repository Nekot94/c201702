shop_list =["ефир","яйца"]
shop_list.append("Молоко")
print(shop_list)
shop_list.pop(1)
print(shop_list)
shop_list[1] = "Аким"
print(shop_list)
animals = "Енот","Лось"
x, y  = animals
print(x)
lox1, lox2 = "Локси", "Лопси"
print(lox2)
games = {"CS6.1","Копатель онлайн","Копатель онлайн", "Копатель онлайн" }
print(games)
best_games = {"HL2","Fallout2","Копатель онлайн"}
print(games & best_games) # Пересечение
print(games | best_games) # Обьединение
print(games - best_games) # Разность

explanatory_dictionary = {"Собака" : "не кошка", "Экзистенциальное":"относящееся к бытию"}
print(explanatory_dictionary["Собака"])
explanatory_dictionary["Креационизм"] = "Учение о том, что мир был создан"
print(explanatory_dictionary["Креационизм"])
explanatory_dictionary[4] = True
print(explanatory_dictionary)