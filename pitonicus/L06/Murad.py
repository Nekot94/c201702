# films = {"Список Шиндлера": "О тяжбах Евреях", "Криминальное чтиво": "об амереканском"}
# print(films["Список Шиндлера"])
# word1 = input("Введите название фильма в словарь ")
# word2 = input("Введите описание фильма в словарь ")
# films[word1] = word2
# print(films)

# c = 0
# while c < 10:
#     c += 1
#     if c == 5:
#         continue
#     print(c)

c = 0
while c < 10:
    c += 1
    if c != 5:
        print(c)

good_guys = ["Чакар", "Роман", "Марат"]

for guy in good_guys:
    print(guy[:-1])

batman = {
    "Имя": "Брюс Вэйн",
    "Возраст": 35,
    "Главный враг": "Календарный человек"
}

# for element in batman:
#     print(element, batman[element])


# for value in batman.values():
#     print(value)

# for k, v in  batman.items():
#     print(k, v)

# for i in range(10):
#     print(i)

# for i in 10:
#     print(i)

# for i in "Артур":
#     print(i)

for i in range(4,10,2):
    print(i)