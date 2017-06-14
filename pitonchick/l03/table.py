import random

random_number = random.randint(0,10)

# answer = int(input("5 * " + \
#     str(random_number) + " = "))
answer = int(input(
    "5 * " + str(random_number) + " = "))

if answer == 5 * random_number:
    print("Ты ответил верно")
else:
    print("Ты ответил неверно")