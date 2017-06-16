def makeShades(alley, k):
    shades = [False for i in range(len(alley))]
    step = 1 if k > 0 else -1
    for i in range(len(alley)):
        if alley[i] <= 0:
            continue
        c = i + alley[i] * k + step
        if c > len(alley):
            c = len(alley)
        if c < 0:
            c = -1
        for j in range(i,c,step):
            shades[j] = True
    return shades

def calculateSunnyLength(shades):
    length = 0
    for shade in shades:
        if not shade:
            length += 1
    return length

def main():
    k = int(input())
    alley = [int(x) for x in input().split(" ")]
    shades = makeShades(alley, k)
    # print(shades)
    length = calculateSunnyLength(shades)
    # print(length)
    result = "Обгорел" if length >= 10 else "Тени достаточно"
    print(result)
    return result

# main()