class Animal:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

    def say(self):
        print("Вэээээээ")

    def attack(self, target):
        print(self.name,"атаковала", target.name)


class Cat(Animal):
    def say(self):
        print("Мяу")

class Dog(Animal):
    def __init__(self, name, kind, loyalty):
        super().__init__(name, kind)
        self.loyalty = loyalty

    def say(self):
        # super().say()
        print("Гав")

    def bite(self, target):
        print(self.name, "укусил", target)

class EvilDog(Dog):
    def bite(self, target):
        super().bite(target)
        print(self.name, "разорвал зубами", target)

class RobotMan:
    def attack(self, target):
        print(self.name,"вынес", target.name)

class AnimalArena:
    def fight(self, animal1, animal2):
        animal1.attack(animal2)
        animal2.attack(animal1)





snow_cat = Cat("Снежок","Британская")
snow_cat.say()

dogchick = EvilDog("Мухтар","Немецкая", '36 / 100')
dogchick.say()
dogchick.bite(snow_cat.name)
print('Преданность: ' + dogchick.loyalty)

arena = AnimalArena()
arena.fight(snow_cat, dogchick)
robot_ksish = RobotMan()
robot_ksish.name = "Кщишь"

arena.fight(robot_ksish, dogchick)
