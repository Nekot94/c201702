class Plant:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def grow(self, years):
        self.age += years

    def show_age(self):
        print(self.name, ":", self.age)

class Tree(Plant):
    def grow(self, years):
        super().grow(years)
        print("Фффффффааааааааааааааааааааафффафаф")

class EvilTree(Tree):
    def kill(self, target):
        print(self.name, "убило и съело", target.name)

  
class Flower(Plant):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.is_bloom = True

    def bloom(self):
        self.is_bloom = True
        print(self.name, "расцвел")

class MutantPlant:
    def __init__(self, plants):
        self.plants = plants

    def show_plants(self):
        print("Я состою из:")
        for plant in self.plants:
            print(plant.name)

    def eat_my_part(self, part):
        if part in self.plants:
            self.plants.remove(part)
            part.grow(1)
        else:
            print("Нечего есть")


class Dubinus:
    def __init__(self):
        self.name = "Дубинус"

    def grow(self, age):
        print("Я дубинус")

spruce = Tree("Чакар", 102, "Ель")
spruce.grow(5)
spruce.show_age() 

maga = Flower("Магомед", 1,"Роза")
maga.grow(3)
maga.show_age()
print(maga.is_bloom)
maga.bloom()
print(maga.is_bloom)

fatima = EvilTree("Фатима", 14, "Береза")
fatima.kill(maga)

dubinus = Dubinus()
arsen = MutantPlant([fatima, spruce, maga, dubinus])
arsen.show_plants()
arsen.eat_my_part(dubinus)
arsen.show_plants()







