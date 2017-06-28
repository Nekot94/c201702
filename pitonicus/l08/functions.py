# def say_hello(name):
#     print("Привет,", name)


# say_hello("Марат")
# say_hello("Никита")

# def sum5(x, y):
#     s = x + y + 5
#     return s

# print(sum5(2, 3))
# x = int(input())
# realy_cool_sum = sum5(x,7)
# print(realy_cool_sum)

# def love_or_kill(target, kill=False):
#     if kill:
#         print(target, "убит")
#     else:
#         print(target, "все любят")

# love_or_kill("Никита", True)
# love_or_kill("Никита")
# love_or_kill(kill=True, target="Никита")
# print("Собака", end=" <3 ")
# print("Собака", end=" ")
# print("1", "3", "2")

# def show_bues(*args, **kwargs):
#     print(args, kwargs)
#     for bue in args:
#         print("Покупка:", bue)
#     for bue in kwargs.values():
#         print("Покупка:", bue)


# show_bues("Тортик", "Ведьмак", "Цветочек")
# show_bues("Тортик", "Ведьмак", best="Цветочек")

def mul5(x, y):
    # global m
    # print(a)
    m = x * y * 5
    return m

def add_element5(super_list):
    # super_list = super_list[:]
    super_list.append(5)

m = 0
a = 5
print(mul5(5, 6))
print(m)

list1 = [5, 6, 7]
add_element5(list1)
print(list1)












