class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age  
    def speak (self,name):
        print("здорово")

    def __str__(self):
        return self.name

    def __iadd__(self, other):
        self.age += other
        return self 

    def __lt__(self, other):
        return self.age < other.age




andrey = Person("Андрей", 26)
said = Person("Саид", 27)
print(andrey)
andrey += 1
print(andrey.age)
print(andrey > said)

    

