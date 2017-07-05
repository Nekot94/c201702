def add_three_exmarks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + "!!!"

    return wrapper

@add_three_exmarks
@add_three_exmarks
@add_three_exmarks
@add_three_exmarks # sum6 = add_three_exmarks(sum6)
def sum6(a, b):
    return a + b + 6


@add_three_exmarks
def say_hello(name):
    return "Привет, " + name + ", лох"


def reverse_sort(e):
    return e[-2]

print(sum6(4, 5))
print(say_hello("Абдушахаев"))
print(add_three_exmarks(sum6)(4, 3))
sum62 = add_three_exmarks(sum6)
print(sum62(4,5))

is_odd = lambda a: bool(a % 2)
print(is_odd(5)) 
print((lambda a: bool(a % 2))(2))
best_boys = ["Магомед_Тагир","Алеша", "гаджиМурад"]
best_boys.sort(key=lambda e: e.lower())
best_boys.sort(key=lambda e: e[-2])
best_boys.sort(key=reverse_sort)
best_boys.sort(key=lambda e: len(e))

print(best_boys)
# print(chr(4667))

