n = int(input())
elems = []
for i in range(n):
    elems.append(int(input()))
for i in range(n-1):
    print(elems[i] + elems[i+1])


