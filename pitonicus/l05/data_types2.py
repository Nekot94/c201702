
# text = "Никогда не сдавайся"
# print(text[11:])
# loves = ['мама', 'папа', 'сестра', 'друг']
# print(loves[1])
# loves.append('братик')
# print(loves)
# loves.pop(2)
# print(loves)
# loves[3] = 0
# print(loves)
dishes = ('суп','пельмени')
soup,  dumplings = dishes
print(soup)
x, y = "морковь", "латук"
print(y)

games = {"ведьмак","крузис3", "веселая ферма", "веселая ферма", "веселая ферма", "веселая ферма"}
print(games)
artur_games = {"cod","csgo","веселая ферма"}
print(games|artur_games) # обьединение
print(games&artur_games) # пересечения
print(games-artur_games) # разность

games = set() # Пустое множество

games_dict = {
    "Ведьмак": "ведьмак и монстры",
    "Дизонред": "О телохранителе и крысах",
    "Фолаут3": "Сын пытается найти отца"
}

print(games_dict["Дизонред"])
games_dict["Skyrim"] = "Драконы и скума"
print(games_dict)
games_dict["Ведьмак"] = "мужик с белыми волосами и всякие кулачные бои"
print(games_dict)