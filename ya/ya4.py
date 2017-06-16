h = int(input())
k = h
for i in range(h):
    k -= 1
    print(" " * k, end="")
    print("*" * ((i + 1) * 2 - 1))
 