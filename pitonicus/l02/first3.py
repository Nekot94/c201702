import math

# sqrt_from_pi = math.sqrt(math.pi)
# print(math.ceil(sqrt_from_pi))

# print(math.factorial(5))
r = int(input("Введите радиус:"))
l = round(2 * math.pi * r, 3)
s = math.pi * r * r
s = round(s, 3)
print ("Длина окружности:", l, "Диаметр:", s)