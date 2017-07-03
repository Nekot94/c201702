# humans = ["Фибо", "Бибо", "Игоб"]
# humans = iter(humans)
# print(humans)
# print(next(humans))
# print(next(humans))
# print(next(humans))
# print(next(humans))
# while True:
#     try:
#         print(next(humans))
#     except StopIteration:
#         break

# for name in humans:
#     print(name)

# numbers = [4, -1, 5, 6, 0]
# numbers = ["", False, 0.0, '', 0]
# print(
#     len(numbers),
#     # sum(numbers),
#     all(numbers),
#     any(numbers),
#     min(numbers),
#     max(numbers))
# bad_names = ["Щамиль","Ибро"]
# good_names = ["Миксим","Морон","Джавид"]
# for bad, good in zip(bad_names, good_names):
#     print(bad, good)

# for aiai, good in enumerate(good_names):
#     print(aiai, good)

# best_numbers = []
# for number in range(1,16):
#     if number%5 != 0:
#         best_numbers.append(number)
# print(best_numbers)
# best_numbers2 = [number for number in range(1,16) if number % 5 != 0]
# print(best_numbers2)

# print(range(5))

# import random

# def random_range(minX, maxX, count):
#     i = 0
#     while i < count:
#         yield random.randint(minX, maxX)
#         i += 1


# print(random_range(1, 4, 5))
# for num in random_range(5, 9, 7):
#     print(num)
def give_letters(count):
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i, letter in enumerate(letters):
        yield letter
        if i == count - 1:
            break

for letter in give_letters(5):
    print(letter)