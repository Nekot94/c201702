name = "Сааду"
number = 8
power = 10.5

print(name,"пошел в гости за:" + str(number) + " миль с милой:" + str(power))
print("%s пошел в гости за:%d миль с милой:%f" %(name, number, power))
print("%4.3s пошел в гости за:%4.3d миль с милой:%4.1f" %(name, number, power))

print("{0} пошел в гости за:{1} миль с милой:{2}".format(name, number, power))
print("{0} пошел в гости за:{0} миль с милой:{0}".format(name, number, power))
print("{0:*^10s} пошел в гости за:{0} миль с милой:{0}".format(name, number, power))

animals = {
    "корова": "муу",
    "собака": "ррр",
    "кошка": "мяу"
}

print("Cобака говорит {0[собака]}, корова говорит {0[корова]}, кошка говорит {0[кошка]} ".format(animals))


# import random
# adv = ["я","свинья", "Саид"]
# word = random.choice(adv)
# print(word)

