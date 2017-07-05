class Human:
    def __init__(self, name, mind, weight, height):
        self.name = name
        self.mind = mind
        self.weight = weight
        self.height = height

    def sit(self, time):
        print(self.name, "сидит", time, "лет")

amir = Human("Амир", True, 40, 150)
print(amir.weight)
amir.weight += 70
print(amir.weight)
amir.sit(10)

amir2 = Human("Эмир", False, 45, 159)
amir2.sit(2)


