import random

class Character:
	def __init__(self, health, attack):
		self.health = health
		self.attack = attack

	def strike(self, target):
		damage = random.randint(0, self.attack)
		target.health -= damage


class Window(Character):

	def die(self):
		print("nhtcr")

class Hero(Character):
	def __init__(self, health, attack):
		super().__init__(health, attack)
		self.count = 0


class Game:
	def start(self):
		hero = Hero(100, 50)
		window = Window(100, 10)
		while True:
			hero.strike(window)
			window.strike(hero)
			print("Жизни игрока:", hero.health)
			print("Жизни окна:", window.health)
			input()
			if window.health <= 0:
				window.die()
				hero.count += 1
				window = Window(100, 10)
			if hero.health <= 0:
				print("Ты сдох, но убил",hero.count, "окон")
				break

game = Game()
game.start()


















