# algebra = {"теорема Пифагора": "gggg", "Равенство треугю": "еееее"}
# print( algebra["теорема Пифагора"])

# sel = 0
# while sel < 10:
#     sel += 1
#     if sel == 5:
#         continue
#     print(sel)

good_boys = ["Ибрагим", "Халид", "Сааду"]
for boy in good_boys:
    print(boy,"хороший")

for number in "10":
    print(number)

user = {
    "имя": "Вова",
    "кошка": True,
    "деньги": 100
}

# for el in user:
#     print(el, user[el])

# for value in user.values():
#     print(value)

for key, value in user.items():   
    print(key, value)

for i in range(5,10,2):
    print(i)