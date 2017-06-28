import random

def create_player():
    player = {"сила":100,"жизни":1000}
    player["имя"] = input("Введите имя: ")
    choise = input("увеличить силу - 1, увеличить жизни - 2 ")
    if choise == "1":
        player["сила"] += 10
    else: 
        player["жизни"] += 100
    return player

def hit(aggressor, victim):
    damage = random.randint(player1["сила"], player1["сила"] + 50)
    victim["жизни"] -= damage
    print("{0[имя]} нанес {2} урона {1[имя]}".format(
        aggressor, victim, damage))

def show_health(player):
    print("{0[имя]} жизни: {0[жизни]}".format(player))

def fight(player1, player2):
    while True:
        hit(player1, player2)
        hit(player2, player1)
        show_health(player1)
        show_health(player2)
        input()
        if player1["жизни"] <= 0:
            print(player2["имя"], "победил")
            break
        if player2["жизни"] <= 0:
            print(player1["имя"], "победил")
            break
            
player1 = create_player()
player2 = create_player()
# print(player1, player2)
fight(player1, player2)