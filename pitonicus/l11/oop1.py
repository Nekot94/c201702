class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def love(self, name):
        print(self.name, "любит", name)

kurban = Human("Курбан",16, "мужчина")
print(kurban.age)
kurban.age += 70
print(kurban.age)
kurban.love("Гильгамеша")

chakar = Human("Чакар",15 , "ж")
print(chakar.gender)
chakar.love("мамка")

