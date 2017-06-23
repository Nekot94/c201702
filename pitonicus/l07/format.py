name = "Рукижат"
number = 42
some = 4.5
print(name,"пошла гулять и купила:" + str(number) + ". Теперь у нас:" + str(some) + " кинжалов")

print("%10.5s пошла гулять и купила:%10.5d. Теперь у нас:%10.2f кинжалов" %(name, number, some))

print("{0} пошла гулять и купила:{1}. Теперь у нас:{2} кинжалов".format(name, number, some))
print("{2} пошла гулять и купила:{0}. Теперь у нас:{0} кинжалов".format(name, number, some))
print("{0:-^10.5s} пошла гулять и купила:{1}. Теперь у нас:{2} кинжалов".format(name, number, some))

user = {
    "имя": "Магомед",
    "фамилия": "Магомедов",
    "возраст": 15
}

print("имя: {0[имя]},\nфамилия {0[фамилия]},\nвозраст {0[возраст]}".format(user))


# import random
# adv = ["Саид","Я", "Молоко"]
# word = random.choice(adv)
# print(word)