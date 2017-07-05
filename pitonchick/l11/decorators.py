def show_em_all(our_func):
    def wrapper(*args, **kwargs):
        print(our_func.__name__)
        print(args)
        print(kwargs)
        result = our_func(*args, **kwargs)
        print(result)
        return result
    return wrapper

def add_3(func):
    def shepard(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + "!!!"

    return shepard

# @add_3
def sum6(a, b):
    return  a + b + 6 

@add_3
@show_em_all
def say_hello(name):
    return "Привет, " + name



# print(sum6(5,3))
# new_sum6 = show_em_all(sum6)
# new_say_hello = show_em_all(say_hello)
# new_sum6(5,2)
# new_say_hello("ПППП")

def sort_left(e):
    return e[-1]

say_hello("Имя")
print(add_3(sum6)(4,3))
print(say_hello("Шеппард"))

sum_words = lambda a, b: a + " и " + b + " лохи"
print(sum_words("Ибоа","Шумиль"))
good_boys = ["умиль", "варис", "Ибра"]
# good_boys.sort(key=lambda e: e.lower())
good_boys.sort(key=lambda e: e[-1])
good_boys.sort(key=sort_left)
print(good_boys)

print(add_3(lambda a: a ** 2)(4))