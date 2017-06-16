n = int(input())
table = []

for i in range(n - 1):
    table.append([int(x) for x in input().split(" ")])

for i in range(n): 
    for k in range(i):
        print(table[i - 1][k], end=" ")
    print(0, end=" ")
    for j in range(i,n - 1):
        print(table[j][i], end=" ")
    print()