from random import randint, choice


class Character:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	def attack(self, other):
		damage = randint(0, self.damage)
		other.hp -= damage
	def show_hp(self):
		print(self.name, "жизни:", self.hp)

class SchoolScum(Character):
	def die(self):
		print(choice(["Школьный визг","Матерится", "взывает к Гамешу"]))

class Hero(Character):
	def __init__(self, name, hp, damage):
		super().__init__(name, hp, damage)
		self.count = 0

class Game:
	def start(self):
		name = input("Введите имя героя: ")
		hero = Hero(name, 190, 15)
		school_scum = SchoolScum("Петя", 55, 3)
		while True:
			hero.attack(school_scum)
			school_scum.attack(hero)
			hero.show_hp()
			school_scum.show_hp()
			input()
			if school_scum.hp <= 0:
				school_scum.die()
				hero.count += 1
				school_scum = SchoolScum("Петя", 55, 3)

			if hero.hp <= 0:
				print ("Герой мёртв!", hero.count, "школьников убито")
				break



game = Game()
game.start()
