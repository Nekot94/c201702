import random
 
class Character:
    def __init__(self, health, attack,armor):
        self.health = health
        self.attack = attack
        self.armor = armor
    def strike(self, target):
        damage = random.randint(0, self.attack - self.armor)
        target.health -= damage
 
 
class Window(Character):
    def die(self):
        print("nhtcr")

    def super_strike(self, target):
        is_bill = random.randint(0,2)
        if (is_bill != 0):
            target.health -= 20
            print("Кара Билла Гейтса\n") 

 
class Hero(Character):
    def __init__(self, health, attack, armor):
        super().__init__(health, attack, armor)
        self.count = 0

    def super_strike(self, target):
        is_heal = random.randint(0,2)
        is_fireball = random.randint(0,2)
        is_lightning = random.randint(0,2)        
        if (is_heal != 0): 
            self.health += 10
            print("Heal\n")    
        if (is_fireball != 0):
            target.health -= 50
            print("Fireball\n")  
        if (is_lightning != 0):
            target.health -= 60
            print("Lighting punch\n")


 
class Game:
    def start(self):
        hero = Hero(100, 50 , 10)
        window = Window(100, 20, 1)
        while True:
            hero.strike(window)
            window.strike(hero)
            hero.super_strike(window)
            window.super_strike(hero)
            print("Жизни игрока:", hero.health)
            print("Жизни окна:", window.health)
            input()
            if window.health <= 0:
                window.die()
                hero.count += 1
                window = Window(100, 20, 10)
            if hero.health <= 0:
                print("Ты сдох, но убил",hero.count, "окон")
                break
 
game = Game()
game.start()