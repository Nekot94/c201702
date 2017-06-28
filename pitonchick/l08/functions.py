# def say_hello(name):
#     print("Привет,", name)

# def sum5(a, b):
#     s = a + b + 5
#     return s


# say_hello("Варис")
# say_hello("Раджаб")

# s = sum5(3,7)
# print(s)


# def kill(target="Варис"):
#     print(target,"убит")

# def kill_them_all(number_of_kills, target="Варис"):
#     print(target, "убит", number_of_kills, "раз")

# kill("Альбина")
# kill()

# kill_them_all(0,"ВВ")
# kill_them_all(target="Ты", number_of_kills=4)

# def show_buy(*args):
#     for buy in args:
#         print(buy)

# show_buy("Сыр","Носки","Кекс")
# show_buy()

# def mul5(a, b):
#     # global c
#     c = a * b * 5
#     return c

# c = 0
# print(mul5(4,5))
# print(mul5(2,3))
# print(c)
# # print(a)

def change_list(list1):
    list1.append(5)

list1 = [3, 4, 6]
change_list(list1)
print(list1)













