import random

def create_player():
    player = {"HP":100, "Damage":10}
    player["name"] = input("Введите имя игрока: ")
    choice = input("1 = Увеличить урон, 2 = Увеличить здоровье: ")
    if choice =="1":
        player["Damage"] += 3
    else:
        player["HP"] += 30
    return player

def strike(attaker, defender):
    damage = random.randint(attaker["Damage"] - 5 , attaker["Damage"] + 5 )
    defender["HP"] -= damage
    print("{0[name]} нанёс {2} урона {1[name]}".format(
        attaker, defender, damage))

def show_HP(player):
    print("{0[name]} жизней:{0[HP]}".format(player))

def fight(player1, player2):
    while True:
        strike(player1, player2)
        strike(player2, player1)
        show_HP(player1)
        show_HP(player2)
        input()
        if player1["HP"] <= 0:
            print(player2["name"], "победил!")
            break
        if player2["HP"] <= 0:
            print(player1["name"], "победил!")
            break

player1 = create_player()
player2 = create_player()

# print(player1, player2)

fight(player1, player2)






