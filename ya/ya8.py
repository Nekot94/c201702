def printMultiplicationTable():
    n = 9
    for i in range(n):
        for j in range(n):
            print((j + 1) * (i + 1), end="")
            if not j == n - 1:
                print("", end="\t")
            else:
                print()


# printMultiplicationTable()