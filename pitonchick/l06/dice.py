import random
player1 = {"счет":0,"ставка":0,"сумма":1000, "бросок":0}
player2 = {"счет":0,"ставка":0,"сумма":1000, "бросок":0}
player1['имя'] = input("Введите имя игрока: ")
player2['имя'] = input("Введите имя игрока: ")

while True:
    player1['ставка'] = int(input("Введите ставку: "))
    if player1["ставка"] > player1["сумма"]:
        player1["ставка"] = player1["сумма"]


    player2['ставка'] = int(input("Введите ставку: "))
    if player2["ставка"] > player2["сумма"]:
        player2["ставка"] = player2["сумма"]

    player1["бросок"] = random.randint(2,12)
    player2["бросок"] = random.randint(2,12)
    print(player1["имя"],player1["бросок"])
    print(player2["имя"],player2["бросок"])

    if player1["бросок"] > player2["бросок"]:
        print(player1["имя"],"выиграл ставку!")
        player1["сумма"] += player2["ставка"]
        player2["сумма"] -= player2["ставка"]
    elif player2["бросок"] > player1["бросок"]:
        print(player2["имя"],"выиграл ставку!")
        player2["сумма"] += player1["ставка"]
        player1["сумма"] -= player1["ставка"]
    else:
        print("Ничья!")
    print(player1["имя"], player1["сумма"])
    print(player2["имя"], player2["сумма"])
    if player1["сумма"] <= 0:
        print(player2["имя"], "победил!")
        break
    if player2["сумма"] <= 0:
        print(player1["имя"], "победил!")
        break