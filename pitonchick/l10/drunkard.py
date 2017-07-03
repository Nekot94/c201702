import random

suits = ["Пики", "Бубны", "Червы", "Крести"]
deck = [(number,suit) for number in range(6,15) for suit in suits]

def get_card(player):
    while True:
        yield player["Колода"].pop()

def turn(player1, player2):
    k = 0
    for card1, card2 in zip(get_card(player1), get_card(player2)):
        k += 2
        print(card1, card2)
        if card1[0] > card2[0]:
            player1["Счет"] += k
            break
        elif card2[0] > card1[0]:
            player2["Счет"] += k
            break


random.shuffle(deck)
print(deck)
player1 = {}
player2 = {}
player1["Колода"] = deck[:len(deck) // 2]
player2["Колода"] = deck[len(deck) // 2:]
player1["Счет"] = 0
player2["Счет"] = 0
while True:
    turn(player1, player2)
    print(player1["Счет"], player2["Счет"])
    input()
    if not player1["Колода"] or not player2["Колода"]:
        break
