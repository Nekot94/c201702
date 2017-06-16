cities = ["Махачкала", "Санта-Моника", "Кельн", "Майами"]
print(cities)
print(cities[2])
print(cities[1:])
cities.append("Амбер")
said_wishes = ["Мачу-Пикчу", "Запретный город"]
cities.extend(said_wishes)
print(cities)
cities.insert(1,"Хасавьюрт")
print(cities)
print(cities.pop(0))
print(cities)
del cities[0]
print(cities)
cities.remove("Кельн")
print(cities)
cities[4] = "Одобренный город"
print(cities)
cities_str = " <3 ".join(cities)
print(cities_str)
print(cities_str.split(" <3 "))
cities.sort(reverse=True)
print(cities)

# cities2 = cities
cities2 = cities[:]
cities2[0] = "Эльфостан"
print(cities2)
print(cities)

vegetables = "Тыква", "Кабачок", "Баклажан"
print(vegetables)
print(vegetables[1])






