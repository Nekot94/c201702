import random

random_number = random.randint(0,10)

a = int(input("5 * " + str(random_number) + " = "))
if a == 5 * random_number:
    print("Правильно!")
else:
    print("ЛОХ")