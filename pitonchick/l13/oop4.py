class Window:
	count = 0

	def __init__(self, width, height, material):
		self.width = width
		self.height = height
		self.material = material
		self.__opacity = 0
		Window.count += 1

	def __del__(self):
		Window.count -= 1


	def is_opening(self):
		print("Я открылось")

	# def set_opacity(self, value):
	# 	if value >= 0:
	# 		self.__opacity = value

	# def get_opacity(self):
	# 	return self.__opacity
	
	@property
	def opacity(self):
		return self.__opacity
	

	@opacity.setter
	def opacity(self, value):
		if value >= 0:
			self.__opacity = value

	@classmethod
	def show_count(cls):
		print(cls.count)

	def say_true():
		print("Ты урод")

	def __iadd__(self, other):
		self.width += other.width
		self.height += other.height
		return self

	def __lt__(self, other):
		return self.width < other.width

	def __str__(self):
		return "Окно из: {0.material} размера: {0.width} на {0.height}".format(self)

class AngryWindow(Window):
	def is_opening(self):
		super().is_opening()
		print("Но ты дебил")






cool_window = Window(2, 5, "plastick")
cool_window.is_opening()
angry_window = AngryWindow(3, 5, "Сыр")
angry_window.is_opening()
angry_window.opacity += 5
print(angry_window.opacity)
peri_and_window = Window(0,0,"red")

# del angry_window
# print(Window.count)
Window.show_count()
Window.say_true()

angry_window += cool_window
print(angry_window.width, angry_window.height)
print(angry_window < cool_window)
print(4)
print(cool_window)